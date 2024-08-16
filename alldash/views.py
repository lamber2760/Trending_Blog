from django.shortcuts import render
# from django.http import HttpResponse
def dashboardd(request):
    return render(request,"dashtemplate/dash_base.html")
def dhblog(request):
    return render(request,"dashtemplate/dhblog.html")
def dh_user(request):
    return render(request,"dashtemplate/dh_user.html")
def dh_addblog(request):
    return render(request,"dashtemplate/dh_addblog.html")
def add_author(request):
    return render(request,"dashtemplate/dh_addauthor.html")



