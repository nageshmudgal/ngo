from django.shortcuts import render,HttpResponse,redirect
from django.contrib.sites.shortcuts import get_current_site
from adminmodule.models import Donations,State,City
from django.http import JsonResponse
from . import settings
from user.models import User
from django.db.models import Sum



import razorpay
razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))


from json import JSONEncoder
from uuid import UUID



def home(request):
    u = User.objects.all()
    l=[]
    l1=[]
    l2=[]
    
    maxi=0
    for i in u:
        d2 = Donations.objects.filter(email=i.email).aggregate(Sum('amount')) 
        if d2["amount__sum"] !=None:
            l.append(d2["amount__sum"])
            l1.append(i)
    if len(l)>2:
        maxi1=max(l)
        u = l.index(maxi1)
        l2.append(l1[u])
        l.remove(maxi1)

        maxi2=max(l)
        u = l.index(maxi2)
        l2.append(l1[u])
        l.remove(maxi2)
        
        maxi3=max(l)
        u = l.index(maxi3)
        l2.append(l1[u])
        l.remove(maxi3)
        
    try:
        user1 = User.objects.get(id=request.session['userid'])
        states = State.objects.all()
        cities = City.objects.all()
        params = {"states": states,"cities":cities,'user1':user1,"topdonars":l2}
        return render(request,"home.html",params)
    except:
        states = State.objects.all()
        cities = City.objects.all()
        params = {"states": states,"cities":cities,"topdonars":l2}
        return render(request,"home.html",params)


        

def donation(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            amt = int(request.POST['amount'])
            ins = Donations(name=name,email=email,amount=amt)
            ins.save()
            callback_url = 'http://'+ str(get_current_site(request))+"/handlerequest/"
            order_currency = 'INR'
            
            razorpay_order = razorpay_client.order.create(dict(amount=amt*100, currency=order_currency, receipt=ins.ordid, payment_capture='0'))
            ins.razorpay_order_id = razorpay_order['id']
            ins.save()
            try:
                if request.session['userid']:
                    user1 = User.objects.get(id=request.session['userid'])
                    return render(request, 'payment.html', {'user1':user1, 'order':ins,  'order_id': razorpay_order['id'],'orderId':ins.ordid, 'final_price':amt, 'razorpay_merchant_id':settings.razorpay_id, 'callback_url':callback_url})
            except:
                return render(request, 'payment.html', {'order':ins,  'order_id': razorpay_order['id'],'orderId':ins.ordid, 'final_price':amt, 'razorpay_merchant_id':settings.razorpay_id, 'callback_url':callback_url})

        return redirect("../")
    except:
        print(request.session['userid'])
        return HttpResponse("505 not found")
    

from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def handlerequest(request):
    
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            try:
                order_db = Donations.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505 Not Found")
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            print(result)
            if result==True:
                print("1")
                amount = order_db.amount * 100   #we have to pass in paisa
                try:
                    print("2")
                    razorpay_client.payment.capture(payment_id, amount)
                    order_db.payment_status = 1
                    order_db.save()

                    
                    try:
                        user1 = User.objects.get(id=request.session['userid'])
                        user1.totaldonation+=order_db.amount
                        user1.save()
                        return render(request, 'paymentsuccess.html',{'id':order_db.id,"user1":user1})
                    except:
                        return render(request, 'paymentsuccess.html',{'id':order_db.id})
                except:
                    order_db.payment_status = 2
                    order_db.save()
                    return render(request, 'paymentfailed.html')
            else:
                order_db.payment_status = 2
                order_db.save()
                return render(request, 'paymentfailed.html')
        except:
            return HttpResponse("505 not found")
