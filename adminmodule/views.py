from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Sum
from .models import Admins,State,City,Member,MemberPost,Org,Campaign,Donations
from branch.models import Branch
from django.core.paginator import Paginator
from user.models import User


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pas = request.POST['pas']
        try:
            user = Admins.objects.get(email=email,password=pas)
            print(user)
            request.session['userid']=user.id
            return redirect("../adminmodule")
        except:
            return redirect("../adminmodule/login")

    return render(request,'adminmodule/login.html')

def logout(request):
    try:
        del request.session['userid']
        return redirect('../')
    except:
        return redirect("../adminmodule/login")


def addadmin(request):
    try:
        if request.session['userid'] !="":
            if request.method == "POST":
                name = request.POST['name']
                email = request.POST['email']
                pas = request.POST['pas']
                ins = Admins(name=name,email=email,password=pas)
                ins.save()

            return render(request,'adminmodule/addadmin.html',{"admin":Admins.objects.get(id=request.session['userid'])})
        else:
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login')
    

def home(request):
    try:
        if request.session['userid'] !="":
            states=State.objects.all()
            cities = City.objects.all()
            branches = Branch.objects.filter(status="Active")
            members = Member.objects.all()
            organisations = Org.objects.all()
            campaigns = Campaign.objects.all()
            donation = Donations.objects.aggregate(Sum('amount'))
            admin = Admins.objects.get(id=request.session['userid'])
            
            params = {"donation":donation,"states":states,"cities":cities,"branches":branches,"campaigns":campaigns,"organisations":organisations,"members":members,"admin":admin}
          
            return render(request,"adminmodule/home.html",params)
        else:
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login')



def deleteinstance(request):
    if request.GET['op']=='1':
        b = request.GET['data']
        Branch.objects.filter(pk=b).update(status="deleted")
        return redirect('branch')
    if request.GET['op']=='2':
        b = request.GET['data']
        Member.objects.filter(pk=b).update(status="deleted")
        return redirect('member')
    if request.GET['op']=='3':
        b = request.GET['data']
        Org.objects.filter(pk=b).update(status="deleted")
        return redirect('org')
    if request.GET['op']=='4':
        b = request.GET['data']
        Campaign.objects.filter(pk=b).update(status="deleted")
        return redirect('campaign')
    return HttpResponse("Error")

from django.db.models import Q

def branch(request):
    try:
        if request.session['userid'] !="":
            branch = Branch.objects.filter(~Q(status="deleted"))
            states = State.objects.all()
            cities = City.objects.all()

            member_paginator = Paginator(branch, 8)
            page_num = request.GET.get('page')
            page = member_paginator.get_page(page_num)

            params={'branch':page,"states": states,"cities":cities,"admin":Admins.objects.get(id=request.session['userid'])}
            
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

            return render(request,'adminmodule/branch.html',params)
        else:
            return redirect('../adminmodule/login')

    except:
        return redirect('../adminmodule/login')

def activatebranch(request):
    try:
        if request.session['userid'] !="":
            b = request.GET['data']
            inactivebranch = Branch.objects.get(pk=b)
            flag=0
            if inactivebranch.status=="Active":
                inactivebranch.status="Inactive"
                flag=1
            if inactivebranch.status=="Inactive" and flag==0:
                inactivebranch.status="Active"
            inactivebranch.save()
            return redirect('../adminmodule/branch')
        else:
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login') 
    
def memberpost(request):
    try:
        posts = MemberPost.objects.all()
        params={"memberposts": posts,"admin":Admins.objects.get(id=request.session['userid'])}

        if request.method == "POST":
            sname = request.POST['sname']
            desc = request.POST['sdesc']
            ins = MemberPost(post=sname, desc=desc)
            ins.save()

        return render(request,'adminmodule/memberpost.html',params)
    except:
        return redirect('../adminmodule/login')

def member(request):
    try:
        posts = MemberPost.objects.all()
        members = Member.objects.filter(status="active")
        
        member_paginator = Paginator(members, 8)
        
        page_num = request.GET.get('page')

        page = member_paginator.get_page(page_num)


        params={"memberposts": posts,"members":page,"admin":Admins.objects.get(id=request.session['userid'])}
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            p = request.POST['post']
            post = MemberPost.objects.get(id=p)
            adress = request.POST['address']
            ins = Member(name=name,email=email,post=post,address=adress)
            ins.save()

        return render(request,'adminmodule/member.html',params)
    except:
        return redirect('../adminmodule/login')

def updatemember(request):
    try:
        user = Admins.objects.get(id=request.session['userid'])
        if request.method == "POST":
            idd = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            p = request.POST['post']
            post = MemberPost.objects.get(id=p)
            adress = request.POST['address']
            
            Member.objects.filter(id=idd).update(name=name,email=email,post=post,address=adress)
            
        return redirect("../adminmodule/member")
    except:
        return redirect('../adminmodule/login')

def updateorg(request):
    try:
        user = Admins.objects.get(id=request.session['userid'])
        if request.method == "POST":
            idd = request.POST['id']
            name = request.POST['name']
            otype = request.POST['otype']
            
            Org.objects.filter(id=idd).update(name=name,otype=otype)

        return redirect("../adminmodule/org")
    except:
        return redirect('../adminmodule/login')

def org(request):
    try:
        o = Org.objects.filter(status="active")

        member_paginator = Paginator(o, 8)
        page_num = request.GET.get('page')
        page = member_paginator.get_page(page_num)

        params={'org':page,"admin":Admins.objects.get(id=request.session['userid'])}
        if request.method == "POST":
            name = request.POST['name']
            otype = request.POST['otype']
            #doj = request.POST['doj']
            ins = Org(name=name,otype=otype)
            ins.save()

        return render(request,'adminmodule/org.html',params)
    except:
        return redirect('../adminmodule/login')

def campaign(request):
    try:
        c = Campaign.objects.filter(status="active")

        member_paginator = Paginator(c, 2)
        page_num = request.GET.get('page')
        page = member_paginator.get_page(page_num)

        params={'campaigns':page,"admin":Admins.objects.get(id=request.session['userid'])}
        if request.method == "POST":
            name = request.POST['name']
            ctype = request.POST['ctype']
            p = request.POST['place']
            i = request.FILES.get('imag')
            d = request.POST['desc']
            ins = Campaign(name=name,ctype=ctype,place=p,img=i,desc=d)
            ins.save()

        return render(request,'adminmodule/campaign.html',params)
    except:
        return redirect('../adminmodule/login')

def viewcamp(request):
    try:
        data = request.GET['data']
        c = Campaign.objects.get(pk=data)
        params={'campaign':c,"admin":Admins.objects.get(id=request.session['userid'])}

        return render(request,'adminmodule/viewcamp.html',params)
    
    except:
        return redirect('../adminmodule/login')

def changepass(request):
    try:
        if request.session['userid'] !="":
            user = Admins.objects.get(id=request.session['userid'])
            if request.method == "POST":
                pas = request.POST['pas']
                Admins.objects.filter(id=request.session['userid']).update(password=pas)

            return render(request,'adminmodule/changepass.html',{"admin":Admins.objects.get(id=request.session['userid'])})
        else:
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login') 

def showdonations(request):
    try:
        if request.session['userid'] !="":
            user = Admins.objects.get(id=request.session['userid'])
            do = Donations.objects.all()
            
            member_paginator = Paginator(do, 8)
            page_num = request.GET.get('page')
            page = member_paginator.get_page(page_num)

            return render(request,'adminmodule/showdonations.html',{"admin":user,"donations":page})
        else:
        
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login')

def showusers(request):
    try:
        if request.session['userid'] !="":
            user = Admins.objects.get(id=request.session['userid'])
            u = User.objects.all()

            member_paginator = Paginator(u, 8)
            page_num = request.GET.get('page')
            page = member_paginator.get_page(page_num)

            return render(request,'adminmodule/showusers.html',{"admin":user,"users":page})
        else:
        
            return redirect('../adminmodule/login')
    except:
        return redirect('../adminmodule/login')