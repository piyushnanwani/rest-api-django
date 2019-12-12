from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .user_api import UserSerialiser
from rest_framework.response import Response
from django.test import Client


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(first_name="", last_name="",company_name="",city="",state="",zip="", email="", web="",age=""):
        if first_name != "" and last_name != "" and company_name !="" and city!="" and state!="" and zip!="" and email!="" and web!="" :
            User.objects.create(first_name = first_name,last_name = last_name,company_name= company_name,city= city,state=state,zip= zip,email = email,web= web,age=age)

    def setUp(self):
        # add test data
        self.create_user("John", "Wick", "The Company ", "LA", "USA", 1234,"iamjohn@company.com","company.com",45 )
        self.create_user("John2", "Wick2", "The Company 2", "LA2", "USA2", 12342,"iamjohn2@company.com","company2.com",46 )


class GetAllUser(BaseViewTest):
    def test_get_all_User(self):
        c = Client()

        #  hit the endpoint
        response = c.get('/api/users/')
        # fetch the data from the db
        expected = User.objects.all()
        serialized = UserSerialiser(expected, many=True)
        
        # self.assertEqual(response.content, serialized.data)
        print(response.content)
        print(serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
