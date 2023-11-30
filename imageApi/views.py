from django.shortcuts import render

# Create your views here.
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ImageUploadForm
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_image = form.save()
        cnn = tf.keras.models.load_model("assets/trained_model3.h5")

        test_set = tf.keras.utils.image_dataset_from_directory(
            'assets/Data/data1/test',
            labels="inferred",
            label_mode="categorical",
            class_names=None,
            color_mode="rgb",
            batch_size=32,
            image_size=(64, 64),
            shuffle=True,
            seed=None,
            validation_split=None,
            subset=None,
            interpolation="bilinear",
            follow_links=False,
            crop_to_aspect_ratio=False,
        )
        image_name = os.path.basename(uploaded_image.image.name)

        image_path = f"media/uploads/{image_name}"
        img = cv2.imread(image_path)

        # Testing Model
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(64, 64))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])  # converting single image to batch
        predictions = cnn.predict(input_arr)
        result_index = np.where(predictions[0] == max(predictions[0]))
        index_0 = result_index[0][0]
        result_name = "{}".format(test_set.class_names[index_0])
        return JsonResponse({'status': 'success', 'image_url': result_name})
