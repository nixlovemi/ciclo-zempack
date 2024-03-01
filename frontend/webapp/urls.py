# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('nosso-negocio', views.negocio),
    path('aerossol-aco', views.aco),
    path('aerossol-aluminio', views.aluminio),
    path('linha-alimenticia', views.alimenticia),
    path('sustentabilidade', views.sustentabilidade),
    path('contato', views.contato),
    path('politica-privacidade', views.privacidade),
    path('news', views.news),
    path('news/<slug:slug>', views.news_detail),
    path('mail', views.mail),
]
