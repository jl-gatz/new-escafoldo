from django.http import JsonResponse


def home(request):
    data = {
        'message': 'API is running!',
        'title': 'checked',
    }
    return JsonResponse(data)
