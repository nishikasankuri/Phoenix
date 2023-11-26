from django.urls import path
from imageApi.views import upload_image

urlpatterns = [
    path('api/upload-image/', upload_image, name='upload_image'),
]