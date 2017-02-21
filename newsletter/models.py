from django.db import models

# Create your models here (rys: essentialy, naming and giving type to a column of a table)
# blank=False means the field is required
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    organization = models.CharField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self): # constructor 
        return self.email

