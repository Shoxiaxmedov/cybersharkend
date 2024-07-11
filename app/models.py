from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Login(models.Model):
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Contact Table"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d")
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # facebook_url = models.CharField(blank=True,max_length=200)
    # twitter_url = models.CharField(blank=True,max_length=200)

    def __str__(self):
        return self.name 

class Dish(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='media//%Y/%m/%d')
    ingredients = models.TextField()
    details = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True)
    is_available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural ="Dish Table"



    class Meta:
        verbose_name_plural="Profile Table"




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='media/dishes/2024')
    # Add other fields as needed

    def str(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
   

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Dish, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    invoice_id = models.CharField(max_length=100, blank=True)
    payer_id = models.CharField(max_length=100, blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.first_name

    class Meta:
        verbose_name_plural = "Order Table"

class Comand(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    name4 = models.CharField(max_length=100)
    comandname = models.CharField(max_length=100)

    def __str__(self):
        return self.comandname
    
# models.py




class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    name = models.CharField(max_length=100)
    item_count = models.IntegerField()

    def str(self):
        return f'{self.user.username} - {self.time} - {self.name} - {self.item_count} item(s)'

class B(models.Model):
    img = models.ImageField(upload_to='media/media/')
    description= models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price
class I(models.Model):
    img = models.ImageField(upload_to='media/')
    description= models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price
class U(models.Model):
    img = models.ImageField(upload_to='media/')
    description= models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price
class T(models.Model):
    img = models.ImageField(upload_to='media/')
    description= models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price



