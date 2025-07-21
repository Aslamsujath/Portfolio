from django.shortcuts import redirect, render
from .models import *
from datetime import datetime
from django.utils.timezone import now

def index(request):
    if request.method == 'POST':
        print("POST received!")
        name = request.POST.get('conName')
        email = request.POST.get('conEmail')
        number = request.POST.get('conPhone')
        service = request.POST.get('conService')
        remarks = request.POST.get('conMessage')

        Contact.objects.create(name=name,email=email,phone_number=number,remarks=remarks,services=service,created_at=datetime.now())
        return redirect('index')
    return render(request, "portfolio_app/index.html")

def about(request):
    return render(request, "portfolio_app/about.html")

def contact(request):
    if request.method == 'POST':
        print("POST received!")
        name = request.POST.get('conName')
        email = request.POST.get('conEmail')
        number = request.POST.get('conPhone')
        service = request.POST.get('conService')
        remarks = request.POST.get('conMessage')

        Contact.objects.create(name=name,email=email,phone_number=number,remarks=remarks,services=service,created_at=datetime.now())
        return redirect('contact')
    return render(request, "portfolio_app/contact.html")

def projects(request):
    return render(request, "portfolio_app/projects.html")

def services(request):
    return render(request, "portfolio_app/services.html")
