from django.db import models

# Create your models here.

GENDER = (("Male","M"), ("Female","F"), ("Others", "O"))

class Login(models.Model):
    user_name = models.CharField(max_length=100, null=True, name="User Name")
    pass_word = models.CharField(max_length=100, null=True, name="Password")
    def __str__(self):
        return str(self.user_name)

class Register(models.Model):
    user_name = models.CharField(max_length=100, null=True, name="User Name")
    email = models.EmailField(max_length=254, null=True, name="Email")
    password = models.CharField(max_length=100, null=True, name="password")
    date_of_birth = models.DateField(null=True, blank=True,name="Date Of Birth")
    gender = models.CharField(max_length=10, choise=GENDER, default="Male", name="Gender")
    nationality = models.CharField(max_length=50, null=True, blank=True, name="Nationality")
    mobile = models.CharField(max_length=15, null=True, blank=True, name="Mobile")
    def __str__(self):
        return str(self.user_name)

class Inbox(models.Model):
    from_email = models.EmailField(max_length=50, null=True, name="From") 
    to_email = models.EmailField(max_length=50, null=True, name="To")
    subject = models.CharField(max_length=100, null=True, blank=True, name="Subject")
    message = models.TextField(max_length=250, blank=True, null=True, name="Message")
    attach = models.FileField(upload_to="attach", max_length=100, name="Attach")
    def __str__(self):
        return str(self.to_email)
