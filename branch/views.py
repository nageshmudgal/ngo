from django.shortcuts import render,redirect
from .models import Branch
from adminmodule.models import State,City

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pas = request.POST['pas']
        try:
            print(email," ",pas)
            user1 = Branch.objects.get(email=email,password=pas,status="Active")
            request.session['userid']=user1.id
            print(user1)
            return redirect("../branch")
        except:
            return redirect("../branch/login")

    return render(request,'branch/login.html')

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
        ins = Branch(bname=name,email=email,password=pas,sid=state,cid=city,address=adress)
        ins.save()

    return render(request,'register.html',params)

def home(request):
    try:
        if request.session['userid'] !="":
            print(request.session['userid'])
            user1 = Branch.objects.get(id=request.session['userid'])

            params={'user1':user1}
            return render(request,"branch/home.html",params)
        else:
            return redirect('../branch/login')
    except:
        return redirect('../branch/login')