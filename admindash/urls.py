from admindash import views
from django.urls import path

urlpatterns =[
    path("",views.homepage),
    path("blog",views.blogs),
    path("addblog",views.addblog),
    path("user",views.user),
    path("addauthor",views.addauthor),
    path("dashboard",views.dashboard),      
]         
