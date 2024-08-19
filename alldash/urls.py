from alldash import views
from django.urls import path

urlpatterns = [
    path("dhboard",views.dashboardd),
    path("dhblog",views.dhblog),
    path("dhaddblog",views.dh_addblog),
    path("dhuser",views.dh_user),
    path("addauthor",views.add_author),
]    