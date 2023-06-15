
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.layout_view, name="layout"),
    path('apresentacao', views.apresentacao_view, name="apresentacao"),
    path('competencias', views.competencias_view, name="competencias"),
    path('formacao', views.formacao_view, name="formacao"),
    path('home', views.home_page_view, name="home"),
    path('projetos', views.projetos_view, name="projetos"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contacto"),
]