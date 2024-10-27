from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/homepage.html')


@login_required(login_url=settings.LOGIN_URL)
def initiatives(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/initiatives.html')
