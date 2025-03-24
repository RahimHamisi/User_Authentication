from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    username=models.CharField(max_length=20,null=True,blank=True,unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?255\d{9}$', 
        message="Phone number must be in the format '+255XXXXXXXXX' with 9 digits after 255"
    )
    phone_number=models.CharField(max_length=13,validators=[phone_regex],null=True,blank=True)
    is_verified=models.BooleanField(default=False)


    def __str__(self):
        return self.username or f"User_{self.id}"
   
class UserProfile(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    def __str__(self):
        return "{self.user.username}-profile's " 

# Continuation of auth_app/models.py
