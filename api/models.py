from django.db import models
from distutils.command.upload import upload
from email.policy import default
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''
    
class Trending(models.Model):
    place_name=models.CharField(max_length=100)
    place_image=CloudinaryField('image')
    place_location=models.CharField(max_length=100)
    trending_item=models.CharField(max_length=100)

    def __str__(self):
        return self.place_name

class Place(models.Model):
    place_name=models.CharField(max_length=100)
    place_image=CloudinaryField('image')
    place_description=models.TextField(max_length=1000)

    def __str__(self):
        return self.place_name

class Activities(models.Model):
    activity_name=models.CharField(max_length=100)
    activity_image=models.URLField(max_length=1000)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    activity_description=models.TextField(max_length=1000)

    def __str__(self):
        return(self.activity_name)

class Festival(models.Model):
    festival_name=models.CharField(max_length=100)
    festival_desc=models.TextField(max_length=1000)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    festival_image=CloudinaryField('image')

    def __str__(self):
        return(self.festival_name)
    
class Item(models.Model):
    item_name=models.CharField(max_length=100)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    item_desc=models.TextField(max_length=300)
    item_image=CloudinaryField('image')
    def __str__(self):
        return(self.item_name)
    
class Purchase(models.Model):
    item_foreign_key=models.ForeignKey(Item,on_delete=models.CASCADE)
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_purchase=models.DateField()

    def __int__(self):
        return(self.item_foreign_key)
    
class Attraction(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    image=CloudinaryField('image')
    desc=models.TextField(max_length=500)
    contact_number=models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
class Booking(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    attact_foreign=models.ForeignKey(Attraction,on_delete=models.CASCADE)
    date=models.DateField()
    image=models.URLField()
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)

class GuideDetail(models.Model):
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    desc=models.TextField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=200)
    contact=models.CharField(max_length=10)
    address=models.TextField(max_length=200)

    def __str__(self):
        return(self.name)

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField(max_length=200)
    message=models.TextField(max_length=2000)

    def __str__(self):
        return(self.subject)
    
class Reviews(models.Model):
    user_foreign = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=1500)
    place_foreign=models.CharField(max_length=30)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return(self.content)
    
class Cuisine(models.Model):
    place_foreign =models.ForeignKey(Place,on_delete=models.CASCADE)
    food_image = CloudinaryField('image')
    food_name = models.CharField(max_length=100)
    
    def __str__(self):
        return(self.food_name)
    
class CulturalEvents(models.Model):
    event_name=models.CharField(max_length=100)
    event_artist=models.CharField(max_length=100)
    event_image=CloudinaryField('image')
    event_desc=models.TextField(max_length=500)
    location=models.CharField(max_length=100)

    def __str__(self):
        return(self.event_name)

class EventBooking(models.Model):
    name_foreign=models.ForeignKey(CulturalEvents,on_delete=models.CASCADE)
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_booking=models.DateField()

    def __int__(self):
        return(self.name_foreign)

class Workshop(models.Model):
    name=models.CharField(max_length=20)
    pic = CloudinaryField('image')
    organizer=models.CharField(max_length=20)
    desc=models.TextField(max_length=1000)
    location=models.CharField(max_length=20)

    def __int__(self):
        return(self.name)
    
class WorkshopBooking(models.Model):
    workshop_foreign=models.ForeignKey(Workshop,on_delete=models.CASCADE)
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_booking = models.DateField()

    def __int__(self):
        return(self.workshop_foreign)
    



