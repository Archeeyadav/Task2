from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class UserProfile(AbstractUser):
    profile = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class CarListing(models.Model):
    company = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    looking_for = models.TextField()  
    specifications = models.TextField()  
    car_type = models.TextField()  
    ppc_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)     


    def __str__(self):
        return self.company
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    max_clicks = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField(default=0)
    standout_features = models.JSONField(default=list)
    amount_charges = models.DecimalField(max_digits=10, decimal_places=2)
    video_url = models.URLField()
    website_url = models.URLField() 
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website_url = models.URLField(blank=True, null=True)
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"