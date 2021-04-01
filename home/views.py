from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    views['projects'] = Project.objects.all()
    views['brands'] = Brand.objects.all()
    return render(request, 'index.html', views)

def about(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    views['brands'] = Brand.objects.all()
    return render(request, 'about.html',views)

def service(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    return render(request, 'services.html', views)

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def bloghome(request):
    return render(request, 'blog-home.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
    views = {}
    views["message"] = "The Form is Submitted."
    views['address'] = Address.objects.all()
    return render(request, 'contact.html',views)