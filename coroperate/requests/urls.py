from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from requests import views


urlpatterns = [
    path('requests/', views.RequestListCreate.as_view()),
    path('users/', views.UserCreate.as_view()),
    path('requests/<int:pk>/', views.RequestUpdate.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
