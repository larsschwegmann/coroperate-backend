from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from requests import views


urlpatterns = [
    path('', views.RequestList.as_view()),
    path('<int:pk>', views.ShoppingItemDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
