from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def landing(request):
    return render(request,"landing.html")
def register(request):
    return render(request,'register.html')
def registerinfo(request):
    if request.method == "POST":
        data = {
            "name" : request.POST.get("name"),
            "email": request.POST.get("email"),
            "date":request.POST.get("date")
        }
        # jsondata = JsonResponse(data)
    return render(request,'registerinfo.html',data)
     

