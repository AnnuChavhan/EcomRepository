from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#settings.py -- url-- customers/welcome ---
from rest_framework.viewsets import ModelViewSet
from customer.models import Customer
from customer.serializers import CustomerSerializer
class CustomerOp(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


'''
from customer.models import Customer
from account.models import Account

def welcome_customer_page(req):
    #return HttpResponse("This is customer welcome page")
    return render(req,'customer.html',
                  {"note" : "Welcome to Customer Portal","cust":dummy_customer()})

def get_list_customer():
    return Customer.objects.all()

def dummy_customer():
    return Customer(id=0,name='',email='',age=0)

def save_or_update(req):
    msg = ''
    if req.method=='POST':
        accid = int(req.POST["account"])
        if accid==0:
            msg="Account Selection is mandatory...!"
            return render(req, 'customer.html',
                          {"cust": Customer(id=req.POST["id"],name=req.POST["name"],age=req.POST["age"],email=req.POST["email"]),
                           "note": msg, "accounts": Account.objects.all(),
                           "customers": Customer.objects.all()})
        else:
            customers = Customer.objects.all()
            for cust in customers:
                if cust.account and cust.account.id==accid:
                    return render(req, 'customer.html',
                                  {"cust": Customer(id=req.POST["id"], name=req.POST["name"], age=req.POST["age"],
                                                    email=req.POST["email"]),
                                   "note": "Account Already assigned to another Customer..!", "accounts": Account.objects.all(),
                                   "customers": Customer.objects.all()})
            if int(req.POST["id"])>0:
                customer = Customer(id=req.POST["id"],name=req.POST["name"],age=req.POST["age"],email=req.POST["email"],account=Account.objects.get(id=accid))
                msg = "Operation Successfully...!"
                customer.save()
            else:
                customer = Customer(name=req.POST["name"], age=req.POST["age"],
                                    email=req.POST["email"],account=Account.objects.get(id=accid) )
                msg = "Add Operation Successfully...!"
                customer.save()

    return render(req, 'customer.html',
                  {"cust":dummy_customer(),
                   "note": msg,"accounts": Account.objects.all(),
                   "customers" : Customer.objects.all()})



def delete_customer(req,cid):
    custob = Customer.objects.get(id=cid)
    custob.delete()
    return render(req, 'customer.html',
                  {"cust": dummy_customer(),
                   "note": "Customer Record Removed Successfully...!",
                   "customers" : Customer.objects.all(),
                   "accounts": Account.objects.all()})

def fetch_customer(req,cid):
    custob = Customer.objects.get(id=cid)
    return render(req, 'customer.html',
                  {"cust": custob,"customers" : Customer.objects.all(),
                   "note": "Customer Record Removed Successfully...!"
                   ,"accounts": Account.objects.all()})
'''