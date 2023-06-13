
from django.urls import path
from .import views
from django.conf.urls.static import static
urlpatterns=[
    path("",views.indexfunction,name="index"),
    path("login",views.loginfunction,name="login"),
    path("packages",views.pacakgesfunction,name="packages"),
    path("register",views.registerfunction,name="register"),
    path("book",views.bookfunction,name="book"),
    path("services",views.servicesfunction,name="services"),
    path("contactus",views.contactusfunction,name="contactus"),
    path("customerregistration",views.customerregister,name="customerregistration"),
    # path("customerbooking",views.customerbook,name="customerbooking"),
    path("customerlogin", views.checkcustlogin, name="customerlogin"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("changepassword",views.changepassword,name="changepassword"),




]