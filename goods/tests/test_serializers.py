from django.test import TestCase

from goods.models import Ads
from goods.serializers import AvitoSerializer


class AvitoSerializerTestCase(TestCase):
    def test_ok(self):
        ads_1 = Ads.objects.create(name='Test ads 1', price=25)
        ads_2 = Ads.objects.create(name='Test ads 2', price=55)
        data = AvitoSerializer([ads_1, ads_2], many=True).data
        expected_data = [
            {
                'id:': ads_1.id,
                'name': 'Test ads 1',
                'price': '25.00'
            },
            {
                'id:': ads_2.id,
                'name': 'Test ads 2',
                'price': '55.00'
            },
        ]
        self.assertEqual(expected_data, data)