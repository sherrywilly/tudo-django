from django.urls import path
from app import views
from django.http import HttpResponse


def about(request):
    return HttpResponse("about")


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',about)
]

