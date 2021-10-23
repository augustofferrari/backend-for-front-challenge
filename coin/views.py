
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, permissions, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coin, CoinReview
from .serializers import (
    CoinListSerializer,
    CoinReviewSerializer,
    CoinReviewUpdateCreateSerializer,
    CoinSerializer,
    UserSerializer,
)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserProfileView(APIView, LoginRequiredMixin):
    """
    Returns user data.
    """

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CoinList(generics.ListAPIView, LoginRequiredMixin):
    queryset = Coin.objects.all()
    serializer_class = CoinListSerializer


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinListSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', "head"]

    @action(
        url_path="reviews",
        detail=True,
        methods=['get'],
        permission_classes=[permissions.IsAuthenticated],
        pagination_class=None)
    def get_review(self, request, *args, **kwargs):
        id = kwargs["pk"]
        self.serializer_class = CoinReviewSerializer
        review_list = Coin.objects.get(id=id).reviews.all()
        user_has_review = CoinReview.objects.filter(
            coin__id=id, user=request.user).exists()
        reviews = CoinReviewSerializer(instance=review_list, many=True)
        return Response(
            {
                "reviews": reviews.data,
                "user_has_review": user_has_review,
            }
        )

    @action(
        url_path="last-added",
        detail=False,
        methods=['get'],
        permission_classes=[permissions.IsAuthenticated],
        pagination_class=None)
    def get_last_added(self, request, *args, **kwargs):
        self.serializer_class = CoinSerializer
        coins = Coin.objects.all().order_by("-created_at")[:4]
        coin_serializer = CoinListSerializer(instance=coins, many=True)
        return Response({"coins": coin_serializer.data})


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = CoinReview.objects.all()
    serializer_class = CoinReviewUpdateCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post", "put", "delete", "head"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        review = CoinReview.objects.get(id=kwargs["pk"])
        if review.user == request.user:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        review = CoinReview.objects.get(id=kwargs["pk"])
        if review.user == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()
