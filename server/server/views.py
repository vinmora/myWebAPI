from django.http import HttpResponse
from django.shortcuts import render



def blog(request):
    str0 = "Hari hari belajar "
    str1 = "Tapi meski capek biar pintar "
    str2 = "biar di masa depan ga cepat modar "
    output = str0 + str1 + str2
    return HttpResponse(output)

def index(request):
    return render(request, "main.html")

def index1(request):
    return HttpResponse("Ini adalah API web saya")




# Create your views here.
