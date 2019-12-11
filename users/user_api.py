from rest_framework import serializers, viewsets
from .models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend

from django.http import HttpResponseRedirect, HttpResponse


class  UserSerialiser(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','company_name', 'city', 'state', 'zip','email', 'web', 'age')

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerialiser
