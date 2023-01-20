from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def my_home(request):
    return HttpResponse('Homepage')


def my_view(request):
    return HttpResponse('About page')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', my_home),
    path("about/", my_view),
]
