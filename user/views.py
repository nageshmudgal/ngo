from django.shortcuts import render,redirect
from .models import User
from django.db.models import Sum
from adminmodule.models import State,City,Donations

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pas = request.POST['pas']
        try:
            print(email," ",pas)
            user1 = User.objects.get(email=email,password=pas,status="Active")
            request.session['userid']=user1.id
            print(user1)
            return redirect("../")
        except:
            return redirect("../")
    return redirect("../")

def logout(request):
    del request.session['userid']
    return redirect('../')

def register(request):
    states = State.objects.all()
    cities = City.objects.all()
    params = {"states": states,"cities":cities}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pas = request.POST['pas']
        s = request.POST['state']
        state = State.objects.get(id=s)
        c = request.POST['city']
        city = City.objects.get(id=c)
        adress = request.POST['address']
        ins = User(uname=name,email=email,password=pas,sid=state,cid=city,address=adress)
        ins.save()
        return redirect('../')
    return redirect('../')

def home(request):
    try:
        if request.session['userid'] !="":
            return redirect('../')
        else:
            return redirect('../')
    except:
        return redirect('../')

def history(request):
    try:
        if request.session['userid'] !="":
            print(request.session['userid'])
            user1 = User.objects.get(id=request.session['userid'])

            
            d = Donations.objects.filter(email=user1.email)
            d2 = Donations.objects.filter(email=user1.email).aggregate(Sum('amount'))
            print(d)
            
            params={'user1':user1,'donation':d,'donations':d2}

            return render(request,"user/history.html",params)
        else:
            return redirect('../user')
    except:
        return redirect('../user')

def changepass(request):
    try:
        if request.session['userid'] !="":
            user1 = User.objects.get(id=request.session['userid'])
            if request.method == "POST":
                pas = request.POST['pas']
                # User.objects.filter(id=request.session['userid']).update(password=pas)
                ins = User.objects.get(id=request.session['userid'])
                ins.password=pas
                ins.save()
            return redirect('../user')
        else:
            return redirect('../user')
    except:
        return redirect('../user')

import os
def profileupdate(request):
    try:
        if request.session['userid'] !="":
            user1 = User.objects.get(id=request.session['userid'])
            if request.method == "POST":
                n = request.POST['uname']
                a = request.POST['address']
                i = request.FILES.get('imag')
                User.objects.filter(id=request.session['userid']).update(uname=n)
                User.objects.filter(id=request.session['userid']).update(address=a)
                if i:
                    image_path = user1.img.path
                    if os.path.exists(image_path):
                        os.remove(image_path)
                    user1.img=i
                    user1.save()
            return redirect('../user')
        else:
            return redirect('../user')
    except:
        return redirect('../user')