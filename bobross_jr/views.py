from django.shortcuts import render
from django.http import JsonResponse
from bobross_jr.models import Birthday

# Create your views here.
def index(request):
    return render(request, 'bobross_jr/index.html')

# TODO: ina view for a request for birthday data
# safe=false needed because not sending back a dict.

def birthday(request):
    birthday = Birthday.objects.all().values()
    birthday_list = list(birthday)
    return JsonResponse(birthday_list, safe=False)

