from django.db import models

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False)
    emailid=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def str(self):
        return self.name

    class Meta:
        db_table = "customer_table"

# class Book(models.Model):
#     name = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(max_length=50, blank=False, unique=True)
#     phone = models.BigIntegerField(blank=False, unique=True)
#     adult = models.IntegerField(blank=False)
#     child = models.IntegerField(blank=False)
#     checkin = models.DateField(blank=False)
#     checkout = models.DateField(blank=False)
#     registrationtime = models.DateTimeField(blank=False, auto_now=True)
#
#     def str(self):
#         return self.name
#
#     class Meta:
#         db_table= "booking_table"