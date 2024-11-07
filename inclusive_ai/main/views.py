import anthropic
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
import httpx


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/homepage.html')


@login_required(login_url=settings.LOGIN_URL)
def initiatives(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/initiatives.html')


@login_required(login_url=settings.LOGIN_URL)
def pears(request: HttpRequest) -> HttpResponse:
    messages = request.GET.get('messages', '')
    word = request.GET.get('word', '')
    
    if not (messages and word):
        return render(request, 'main/pears.html')

    PROXIES = {}

    if settings.AI_PROXY:
        PROXIES['all://'] = settings.AI_PROXY

    client = anthropic.Anthropic(
        api_key=settings.ANTHROPIC_API_KEY,
        # http_client=httpx.Client(proxies=PROXIES),
    )
    
    response = client.messages.create(
        model='claude-3-haiku-20240307',
        max_tokens=200,
        temperature=0.7,
        system='''ты генератор сказок, для детей 2-5 лет, в ней пропусти слова которые очевидны для замены, 5 слов Машеньку сказку, каждое предложение должно состоять из 1-3 слов, пропущенные слова выпиши ниже в формате 1) (слово первой замены)
2) (слово второй замены)
В места пропушенных слов ставь цифры
Придумывай сказки с инетерсными сюжетами каждый раз разный''',
        messages=[{'role': 'user', 'content': f'описание сказки: {messages}\n\nслово для изучения: {word}'}],
    )
    response = response.content[0].text.strip()
    
    return render(request, 'main/pears-generate.html', context={
        'response': response,
        'messages': messages,
        'word': word,
    })


@login_required(login_url=settings.LOGIN_URL)
def diagnostic_test(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/diagnostic-test.html')


@login_required(login_url=settings.LOGIN_URL)
def test_question(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/test-question.html', {
        'question_title': '2 + 2 = ?',
        'answers': ['2', '4', '22', '5'],
    })
