from django.http import JsonResponse

def test_endpoint(request):
    return JsonResponse({'status': 'ok'})
