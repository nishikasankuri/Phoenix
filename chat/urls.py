from django.urls import path
from .views import chat_with_gpt3

urlpatterns = [
    path('api/get-data/', chat_with_gpt3, name='chat_view'),
]