from django.shortcuts import render

# Create your views here.

def home(request):
 return render(request, 'app/home.html')

def login(request):
 return render(request, 'app/login.html') 

def contact(request):
 return render(request, 'app/contact.html')  

def about(request):
 return render(request, 'app/about.html') 

def search(request):
 return render(request, 'app/search.html') 

def cart(request):
 return render(request, 'app/cart.html') 


