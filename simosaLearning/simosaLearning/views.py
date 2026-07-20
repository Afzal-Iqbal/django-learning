from django.http import HttpResponse

def home(request):
    return HttpResponse("hello, world. i am learning django for the second time")

def about(request):
    return HttpResponse("This is about page of django page")


def contact(request):
    return HttpResponse("Contact page is here ")