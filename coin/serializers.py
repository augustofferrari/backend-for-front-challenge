from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Coin, CoinReview


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]


class CoinListSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"


class CoinSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = ["name", "abbreviation"]


class CoinReviewSerializer(ModelSerializer):
    user = UserSerializer()
    coin = CoinSerializer()

    class Meta:
        model = CoinReview
        fields = "__all__"


class CoinReviewUpdateCreateSerializer(ModelSerializer):

    class Meta:
        model = CoinReview
        fields = ["coin", "text", "ranking"]
