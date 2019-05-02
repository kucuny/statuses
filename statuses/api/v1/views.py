from django.http import JsonResponse


def t(request):
    return JsonResponse({'a': 1})
