
from django.urls import path
from Blog import views

urlpatterns = [
    path("",views.homepage),
    path("about",views.aboutus),
    path("services",views.services),
    path("contact",views.contact),
    path("trending_blog",views.trendingblog),
    path("blog",views.blog),
    path("login",views.login),
    path("signup",views.signup),
]
