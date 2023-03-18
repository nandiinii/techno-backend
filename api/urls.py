from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BlacklistTokenView,LoggedInUserView,RegisterView,TrendingViewSet,PlaceView,ActivitiesView,FestivalViewSet,ItemViewSet,PurchaseViewSet,AttractionViewSet,BookingViewSet,GuideDetailViewset,ContactViewSet,ReviewViewSet,CuisineViewSet,EventViewSet,EventBookViewSet,WorkshopBookingViewSet,WorkshopViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('trendings',TrendingViewSet,basename='trendings')
router.register('places',PlaceView,basename='places')
router.register('activities',ActivitiesView,basename='activities')
router.register('festivals',FestivalViewSet,basename='festivals')
router.register('items',ItemViewSet,basename='items')
router.register('purchases',PurchaseViewSet,basename='purchases')
router.register('attractions',AttractionViewSet,basename='attractions')
router.register('booking',BookingViewSet,basename='booking')
router.register('guides',GuideDetailViewset,basename='guides')
router.register('contacts',ContactViewSet,basename='contacts')
router.register('reviews',ReviewViewSet,basename='reviews')
router.register('cuisine',CuisineViewSet,basename='cuisine')
router.register('cultural-event',EventViewSet,basename='cultural-event')
router.register('event-booking',EventBookViewSet,basename='event-booking')
router.register('workshop',WorkshopViewSet,basename='workshop')
router.register('workshop-booking',WorkshopBookingViewSet,basename='workshop-booking')

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]