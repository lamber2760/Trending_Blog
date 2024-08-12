from django.shortcuts import render


def homepage(request):
    return render(request,"home-alt.html")

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def allreview(request):
    return render(request,"review.html")

def trendingblog(request):
    return render(request,"treanding-blog.html")
def blog(request):
    return render(request,"blog.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")



