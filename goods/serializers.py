from rest_framework.serializers import ModelSerializer

from goods.models import Ads


class AvitoSerializer(ModelSerializer):
    class Meta:
        model = Ads
        fields = ['name', 'created_at', 'price', 'view']