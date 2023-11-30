import openai
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
@require_POST
def chat_with_gpt3(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        value = data.get('data', '')
        value = value.strip()
        print(value)
        openai_response = generate_openai_response(value)
        print(openai_response)
        return JsonResponse({'response': openai_response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def generate_openai_response(user_input):
    # Set your OpenAI API key
    openai.api_key = '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'

    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt="Explain not more than 70 words about the plant " + " " + user_input + " " + " and name their nomenclature ",
        max_tokens=100 # Adjust based on your needs
    )

    return response['choices'][0]['text']