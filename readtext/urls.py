from django.urls import path

from readtext.views import read_text
urlpatterns = [
    path('api/read-text/', read_text, name='chat_view'),
]