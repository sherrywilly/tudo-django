from django.urls import path
from app import views
from django.http import HttpResponse





urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:crud_id>',views.update,name='update'),
    path('delete/<int:crud_id>',views.delete,name='delete'),
]

