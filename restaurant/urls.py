from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, RegisterUserView

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegisterUserView.as_view(), name='registration'),
]
