# ride/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideMatchingView, RideStatusUpdateView, RideViewSet
from .views import UserRegistrationView, UserLoginView


router = DefaultRouter()
router.register(r'rides', RideViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
    path('rides/<int:pk>/status/', RideStatusUpdateView.as_view(), name='ride-status-update'),
    path('rides/match/', RideMatchingView.as_view(), name='ride-match'),
]
