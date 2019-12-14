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


class  UserSerialiser(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','company_name', 'city', 'state', 'zip','email', 'web', 'age')



class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerialiser
    
    #search 
    filter_backends = (DjangoFilterBackend,)
    
    # pagination 

    # filter_fields = ('first_name', 'last_name')
    pagination_class = LimitOffsetPagination
    

    def get_queryset(self):
        queryset = User.objects.all()
        sort_by = self.request.query_params.get('sort', None)
        name_search = self.request.query_params.get('name', None) 

        if sort_by is not None:
            queryset = queryset.order_by(sort_by)
        
        if name_search is not None:
            queryset = queryset.filter(first_name=name_search) 

        return queryset
