from django.db import models
from adminmodule.models import State,City

class Branch(models.Model):

    bname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sid = models.ForeignKey(State,on_delete=models.CASCADE,default=1)
    cid = models.ForeignKey(City,on_delete=models.CASCADE,default=1)
    password = models.CharField(max_length=50,default='12345')
    address = models.CharField(max_length=500,default="india")
    status = models.CharField(max_length=10,default="Inactive")

    def __str__(self):
        return self.bname
