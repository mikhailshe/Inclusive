from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/homepage.html')


@login_required(login_url=settings.LOGIN_URL)
def initiatives(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/initiatives.html')


@login_required(login_url=settings.LOGIN_URL)
def pears(request: HttpRequest) -> HttpResponse:
    messages = request.GET.get('messages', '')
    word = request.GET.get('word', '')

    if messages and word:
        return render(request, 'main/pears-generate.html', context={
            'messages': messages,
            'word': word,
        })
    
    return render(request, 'main/pears.html')
    
