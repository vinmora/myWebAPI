from django.shortcuts import HttpResponse

def index(request):
    str0 = "Hari hari belajar "
    str1 = "Tapi meski capek biar pintar "
    str2 = "biar di masa depan ga cepat modar "
    output = str0 + str1 + str2
    return HttpResponse(output)

def blog(request):
    return HttpResponse("Ini adalah halaman blog")



# Create your views here.
