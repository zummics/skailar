from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('report-abuse/', abuse, name='abuse'),
    path('domains/', domain, name='domain'),
    path('game-servers/', gameservers, name='gameservers'),
    path('contact-us/', contact, name='contact'),
    path('register/', registerPage, name='register'),
    path('terms/', terms, name='terms'),
]

handler404 = 'app.views.handler404'