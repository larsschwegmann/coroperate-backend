from django.urls import path
from shopping import views

urlpatterns = [
    path('', views.login_page)
]