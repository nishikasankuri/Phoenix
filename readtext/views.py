import pyttsx3
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST

import logging
from gtts import gTTS
import os

# Create your views here.
logger = logging.getLogger(_name_)


@csrf_exempt
@require_POST
def read_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        language = data[0]['language']
        value = data[1]['data']
        logger.info(language)
        logger.info(value)
        tts = gTTS(text=value, lang=language, slow=False)
        tts.save("output.mp3")
        os.system("start output.mp3")
        return JsonResponse({'response': 'Reading Text'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
