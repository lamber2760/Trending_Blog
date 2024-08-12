from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"home.html")
def dashboard(request):
    return render(request,"dashboard.html")
def blogs(request):
    return render(request,"blog.html")
def addauthor(request):
    return render(request,"add_author.html")
def addblog(request):
    return render(request,"add_blog.html")
def user(request):
    return render(request,"users.html")
