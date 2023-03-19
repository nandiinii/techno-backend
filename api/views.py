from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import User,Trending,Place,Activities,Item,Festival,Purchase,Attraction,Booking,GuideDetail,Contact,Reviews,Cuisine,EventBooking,CulturalEvents,Workshop,WorkshopBooking
from .serializers import UserSerializer,RegisterSerializer,TrendingSerializer,PlaceSerializer,ActivitiesSerializer,FestivalSerializer,ItemSerializer,GuideSerializer,PurchaseSerializer,AttractionSerializer,BookingSerializer,ContactSerializer,ReviewsSerializer,CuisineSerializer,EventBookingSerializer,CulturalEventSerializer,WorkshopSerializer,WorkshopBookingSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
# Create your views here.

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class ActivitiesView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=ActivitiesSerializer
    queryset=Activities.objects.all()

class PlaceView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PlaceSerializer
    queryset=Place.objects.all()

class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class FestivalViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=FestivalSerializer
    queryset=Festival.objects.all()

class ItemViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=ItemSerializer
    queryset=Item.objects.all()


class PurchaseViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseSerializer
    queryset=Purchase.objects.all()

class AttractionViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=AttractionSerializer
    queryset=Attraction.objects.all()

class BookingViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class= BookingSerializer
    queryset=Booking.objects.all()

class GuideDetailViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=GuideSerializer
    queryset=GuideDetail.objects.all()
    
class ContactViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()

class ReviewViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class CuisineViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=Cuisine.objects.all()
    serializer_class=CuisineSerializer

class EventBookViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=EventBookingSerializer
    queryset=EventBooking.objects.all()

class EventViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset=CulturalEvents.objects.all()
    serializer_class=CulturalEventSerializer

class WorkshopViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=WorkshopSerializer
    queryset=Workshop.objects.all()  

class WorkshopBookingViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=WorkshopBookingSerializer
    queryset=WorkshopBooking.objects.all()    




    


