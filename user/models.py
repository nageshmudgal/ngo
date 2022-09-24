from django.db import models
from adminmodule.models import State,City

class User(models.Model):

    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sid = models.ForeignKey(State,on_delete=models.CASCADE,default=1)
    cid = models.ForeignKey(City,on_delete=models.CASCADE,default=1)
    password = models.CharField(max_length=50,default='12345')
    address = models.CharField(max_length=500,default="india")
    img=models.ImageField(upload_to='user/', default='user/userprofile.jpg')
    status = models.CharField(max_length=10,default="Active")
    totaldonation = models.FloatField(default=0)

    def __str__(self):
        return self.uname
