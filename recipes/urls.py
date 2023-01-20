from django.urls import path

from recipes.views import contacts, home

urlpatterns = [
    path('', home),
    path("contatos/", contacts),
]
