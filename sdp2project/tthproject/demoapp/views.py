from django.db.models import Q
from django.shortcuts import render

from .models import Customer


def indexfunction(request):
    return render(request,"index.html")
def loginfunction(request):
    return render(request,"login.html")
def registerfunction(request):
    return render(request,"register.html")
def pacakgesfunction(request):
    return render(request,"pacakges.html")
def bookfunction(request):
    return render(request, "book.html")
def servicesfunction(request):
    return render(request, "services.html")
def contactusfunction(request):
    return render(request, "contactus.html")
def userlogout(request):
    return render(request,"login.html");
def changepassword(request):
    return render(request,"changepwd.html")

def customerregister(request):
    name=request.POST["name"]
    email = request.POST["emailid"]
    username = request.POST["username"]
    password=request.POST["password"]
    contact = request.POST["contactno"]
    location = request.POST["location"]
    customerobj = Customer(name=name,emailid=email,username=username,password=password,contact=contact,location=location)
    Customer.save(customerobj)
    print(customerobj)

    msg='Customer registered successfully'
    return render(request, "register.html", {"msg": msg})

# def customerbook(request):
#     name=request.POST["name"]
#     email=request.POST["email"]
#     phone=request.POST["phone"]
#     adult=request.POST["adult"]
#     child=request.POST["child"]
#     checkin=request.POST["checkin"]
#     checkout=request.POST["checkout"]
#     customerobj1=Book(name=name,email=email,phone=phone,adult=adult,child=child,checkin=checkin,checkout=checkout)
#     Book.save(customerobj1)
#     print(customerobj1)
#
#     msg="Booking successfull"
#     return render(request,"https://rzp.io/l/ia2RvwVhrd",{"msg":msg})


def checkcustlogin(request):
    email= request.POST["emailid"]
    pwd= request.POST["password"]

    flag = Customer.objects.filter(Q(emailid=email) & Q(password=pwd))

    print(flag)

    if flag:
        cust = Customer.objects.get(emailid=email)
        print(cust)
        print(cust.id,cust.name)
        request.session["cid"] = cust.id
        request.session["cname"] = cust.name
        return render(request, "customer.html", {"cid": cust.id, "cname": cust.name})
        print("login success")
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})


def empupdatepwd(request):
    eid=request.session["id"]
    ename=request.session["name"]

    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag = Customer.objects.filter(Q(id=eid) & Q(password=opwd))

    if flag:
        Customer.objects.filter(id=eid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "changepwd.html", {"id": eid, "ename": ename,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "changepwd.html", {"id": eid, "ename": ename,"msg":msg})

