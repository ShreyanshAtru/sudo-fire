from django.contrib import admin
from django.urls import path
from .views import UserApiView

urlpatterns = [
    path('user-view', UserApiView.as_view()),
]
