from rest_framework import serializers
from .models import User,Trending,Place,Activities,Item,Festival,Purchase,Attraction,Booking,GuideDetail,Contact,Reviews,Cuisine,CulturalEvents,EventBooking,Workshop,WorkshopBooking
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class TrendingSerializer(serializers.ModelSerializer):
    place_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Trending
        fields='__all__'

class PlaceSerializer(serializers.ModelSerializer):
    place_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Place
        fields='__all__'

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Activities
        fields='__all__'

class FestivalSerializer(serializers.ModelSerializer):
    festival_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Festival
        fields='__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model=GuideDetail
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    item_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Item
        fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields='__all__'

class AttractionSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Attraction
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'

class CuisineSerializer(serializers.ModelSerializer):
    food_image = serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Cuisine
        fields = '__all__'

class CulturalEventSerializer(serializers.ModelSerializer):
    event_image = serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=CulturalEvents
        fields = '__all__'

class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventBooking
        fields='__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    pic = serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
         model=Workshop
         fields = '__all__'

class WorkshopBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkshopBooking
        fields='__all__'







