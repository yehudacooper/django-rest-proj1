from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

    def get_queryset(self):
        queryset = models.UserProfile.objects.all()
        countryname = self.request.query_params.get('country',None)
        cityname = self.request.query_params.get('city',None)
        addressname = self.request.query_params.get('address',None)


        if countryname is not None:
            queryset = queryset.filter(country_id__name = countryname)
            return queryset

        if cityname is not None:
            queryset = queryset.filter(city_id__name = cityname)
            return queryset

        if addressname is not None:
            queryset = queryset.filter(address_id__name = addressname)
            return queryset

        return queryset



class LoginViewSet(viewsets.ViewSet):

    # serializer_class = AuthTokenSerializer
    get_serializer = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken.post(self,request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):

     authentication_classes = (TokenAuthentication,)
     serializer_class = serializers.ProfileFeedItemSerializer
     queryset = models.ProfileFeedItem.objects.all()
     permission_classes = (permissions.PostOwnStatus,IsAuthenticated)
     def perform_create(self, serializer):

         serializer.save(user_profile = self.request.user)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer

    def get_queryset(self):
        # if countryname == 'all':
            queryset = models.Country.objects.all()
            return queryset