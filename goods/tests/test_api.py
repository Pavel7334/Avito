from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from goods.models import Ads, Category
from goods.serializers import AvitoSerializer


class AvitoApiTestCase(APITestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(title='Category_1')
        self.category_2 = Category.objects.create(title='Category_2')
        self.ads_1 = Ads.objects.create(name='Test ads 1', price=25,
                                        category=self.category_1)
        self.ads_2 = Ads.objects.create(name='Test ads 2', price=55,
                                        category=self.category_1)
        self.ads_3 = Ads.objects.create(name='Test ads 2', price=55,
                                        category=self.category_2)

    def test_get(self):

        url = reverse('ads-list')
        response = self.client.get(url)
        serializer_data = AvitoSerializer([self.ads_1, self.ads_2, self.ads_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):

        url = reverse('ads-list')
        response = self.client.get(url)
        serializer_data = AvitoSerializer([], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)