from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello, world. i am learning django for the second time")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is about page of django page")


def contact(request):
    return HttpResponse("Contact page is here ")