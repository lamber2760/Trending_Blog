from django.shortcuts import render


def homepage(request):
    return render(request,"home-alt.html")

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def trendingblog(request):
    return render(request,"treanding-blog.html")

def blog(request):
    return render(request,"blog.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")



