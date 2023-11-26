from django.http import JsonResponse


def welcome(request):
    message = {'message': 'Welcome to the Django Simple Endpoint!'}
    return JsonResponse(message)