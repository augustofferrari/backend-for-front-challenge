
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CoinViewSet, ReviewsViewSet, UserProfileView

router = DefaultRouter(trailing_slash=False)
router.register('coins', CoinViewSet)
router.register("reviews", ReviewsViewSet)


urlpatterns = [
    path('user-profile', UserProfileView.as_view()),
] + router.urls
