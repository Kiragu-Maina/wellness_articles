from django.urls import path
from . import views

urlpatterns = [
    path('get-articles/', views.ArticlesView.as_view(), name='get-articles'),
]
