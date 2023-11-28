from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.decorators.http import require_POST
from googletrans import Translator
import logging

# Create your views here.
logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
def translate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        language = data[0]['language']
        value = data[1]['data']
        logger.info(language)
        logger.info(value)
        translator = Translator()
        text_to_translate = value
        translated_text = translator.translate(text_to_translate, dest=language).text
        logger.info(translated_text)
        return JsonResponse({'response': translated_text})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
