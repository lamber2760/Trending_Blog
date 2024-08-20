from django.db import models

class blogdashboard(models.Model):
    title = models.TextField("max_length = 60")
    blog  = models.TextField("max_length = 120")
    myimg = models.ImageField(upload_to="userprofilr",null=True,blank=True)

