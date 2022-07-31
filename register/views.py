from django.shortcuts import render
from django.http import HttpResponse
from register.models import Person
# Create your views here.

def home(request):
    payload = {'persons': Person.objects.all()}
    return render(request, 'home.html', payload)

def register_form(request):
    return render(request, 'register.html')

def save_result(request):
    payload = {
        "inputFirstname": request.POST["inputFirstname"],
        "inputLastname": request.POST["inputLastname"],
        "inputAddress": request.POST["inputAddress"],
    }
    p = Person(
        firstname=payload['inputFirstname'],
        lastname=payload['inputLastname'],
        address=payload['inputAddress'],
    )
    p.save()
    return render(request, 'save-result.html', payload)


