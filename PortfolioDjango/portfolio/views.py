#  hello/views.py

from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def layout_view(request):
    return render(request, 'portfolio/layout.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')

def competencias_view(request):
    return render(request, 'portfolio/competencias.html')
def blog(request):
    return render(request, 'portfolio/blog.html')
def contact(request):
    return render(request, 'portfolio/contact.html')

