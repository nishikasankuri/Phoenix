from django.urls import path

from translate.views import translate

urlpatterns = [
    path('api/translate-data/', translate, name='translate'),
]