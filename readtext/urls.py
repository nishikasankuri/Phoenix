from django.urls import path

from readText.views import read_text
urlpatterns = [
    path('api/read-text/', read_text, name='chat_view'),
]