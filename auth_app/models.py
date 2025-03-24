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


    # Fix reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_app_user_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_app_user_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username or f"User_{self.id}"
   
class UserProfile(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    def __str__(self):
        return "{self.user.username}-profile's " 

# Continuation of auth_app/models.py
class Role(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='auth_app_role_permissions')

    def __str__(self):
        return self.name

class UserRole(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username or 'Unnamed'} - {self.role.name}"