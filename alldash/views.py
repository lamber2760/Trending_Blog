from django.shortcuts import render,redirect
from alldash.models import blogdashboard
# from django.http import HttpResponse
def dashboardd(request):
    return render(request,"dashtemplate/dash_base.html")
def dhblog(request):
    data = blogdashboard.objects.all().order_by("-id")
    context={"mydata":data}
    return render(request,"dashtemplate/dhblog.html",context)

def dh_user(request):
    return render(request,"dashtemplate/dh_user.html")
def dh_addblog(request):
    return render(request,"dashtemplate/dh_addblog.html")
def add_author(request):
    return render(request,"dashtemplate/dh_addauthor.html")


def allsavedata(request):
    if request.method == "POST":
        usertitle = request.POST.get("firsttitle")
        userblog  = request.POST.get("firstblog")
        allimg = request.FILES.get("img")
        data = blogdashboard(title = usertitle, blog = userblog,  myimg = allimg)
        data.save()
    
    return redirect("review")

def deletedata(request,kgf):
    mydata  = blogdashboard.objects.get(id=kgf)
    mydata.delete()
    return redirect("review")
def updatedata(request,asd):
    data = blogdashboard.objects.get(id =asd)
    return render(request,"dashtemplate/updatedhblog.html",{"meandata":data})
def nowudatedata(request,up):
    if request.method == "POST":
        usertitle = request.POST.get("firsttitle")
        userblog  = request.POST.get("firstblog")
        userimg = request.FILES.get("img")
        my__data = blogdashboard.objects.get(id=up)
        my__data.title = usertitle
        my__data.blog = userblog
        my__data.allimg = userimg
        my__data.save()
    return redirect("review")    
        



