from rest_framework.pagination import LimitOffsetPagination
from rest_framework import serializers, viewsets
from .models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

import django_filters
from django_filters import filters

class  UserSerialiser(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','company_name', 'city', 'state', 'zip','email', 'web', 'age')



class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerialiser
    
    #search 
    search_fields = ('first_name', 'last_name')
    filter_backends = (DjangoFilterBackend,SearchFilter)
    
    # pagination 
    pagination_class = LimitOffsetPagination
    

    def get_queryset(self):
        queryset = User.objects.all()
        sort_by = self.request.query_params.get('sort', None)

        if sort_by is not None:
            queryset = queryset.order_by(sort_by)
        
        return queryset
