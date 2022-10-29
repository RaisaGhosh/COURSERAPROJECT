from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")