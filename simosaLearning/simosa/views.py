from django.shortcuts import render

# Create your views here.
def all_simosa(request):
    return render(request, 'simosa/all_simosa.html')
    