from django.db import models
import uuid
from django.utils import timezone
class Admins(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50,default='12345')
    status = models.CharField(max_length=10,default="active")

    def __str__(self):
        return self.name


class State(models.Model):

    name = models.CharField(max_length=50)
    sdesc = models.CharField(max_length=100,default="-")

    def __str__(self):
        return self.name


class City(models.Model):

    sid = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MemberPost(models.Model):

    post = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    

    def __str__(self):
        return self.post

class Member(models.Model):

    name = models.CharField(max_length=50)
    # mob = models.IntergerFeild(max_length=12)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500,default="india")
    post = models.ForeignKey(MemberPost,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,default="active")

    def __str__(self):
        return self.name

class Org(models.Model):
    name = models.CharField(max_length=50)
    otype = models.CharField(max_length=20)
    # doj = models.DateField()
    doj = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=10,default="active")    
    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    ctype = models.CharField(max_length=20)
    date = models.DateField(auto_now=True, auto_now_add=False)
    place = models.CharField(max_length=100)
    img = models.ImageField(upload_to="campaign/", default='')
    desc = models.CharField(max_length=1000)
    status = models.CharField(max_length=10,default="active")

    def __str__(self):
        return self.name

class Donations(models.Model):
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    ordid = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    amount = models.FloatField()
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.ordid is None and self.datetime_of_payment and self.id:
            self.ordid = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


    def __str__(self):
        return str(self.ordid)