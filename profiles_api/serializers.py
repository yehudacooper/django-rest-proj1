from rest_framework import serializers
from .models import Country,City,Address

from . import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password','country','city','address','country_id','city_id','address_id')
        extra_kwargs = {'password':{'write_only':True},'country_id':{'read_only':True},'city_id':{'read_only':True},'address_id':{'read_only':True},}
        depth = 1

    def create(self,validated_data):
        if not Country.objects.filter(name=validated_data['country']).exists():
                country = models.Country(name = validated_data['country'])
                country.save()

        if not City.objects.filter(name=validated_data['city']).exists():
                city = models.City(name = validated_data['city'])
                city.save()

        if not Address.objects.filter(name=validated_data['address']).exists():
                address = models.Address(name = validated_data['address'])
                address.save()

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
            country=validated_data['country'],
            city=validated_data['city'],
            address=validated_data['address'],
            country_id=models.Country.objects.filter(name =validated_data['country'])[0],
            city_id = models.City.objects.filter(name=validated_data['city'])[0],
            address_id = models.Address.objects.filter(name=validated_data['address'])[0]

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name')

















class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
