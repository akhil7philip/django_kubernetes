from django.test import TestCase

from .models import PollsModel
# Create your tests here.
class PollsTest (TestCase):
    def setUp(self):
        PollsModel.objects.create(name='Aks')
        
    def test_case(self):
        q = PollsModel.objects.all()
        self.assertTrue(q.exists())