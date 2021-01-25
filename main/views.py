from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world!")

def homework(request):
    return render(request, "1.html")
