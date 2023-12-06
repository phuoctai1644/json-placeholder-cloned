from rest_framework import serializers
from users.models import User, Address, Geo, Company

class GeoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Geo
    fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
  geo = GeoSerializer()

  class Meta:
    model = Address
    fields = ['street', 'suite', 'city', 'zipcode', 'geo']
    
  def create(self, validated_data):
    geo_data = validated_data.pop('geo')
    # Dữ liệu đầu vào cho `Geo` là đơn giản, không cần xử lí nhiều trường
    # Dùng objects thay cho serializer đầy đủ
    geo_instance = Geo.objects.create(**geo_data)
    return Address.objects.create(geo=geo_instance, **validated_data)
  
  def update(self, instance, validated_data):
    geo_serializer = self.fields['geo']
    geo_instance = instance.geo

    geo_data = validated_data.pop('geo')
    geo_serializer.update(geo_instance, geo_data)
    return super(AddressSerializer, self).update(instance, validated_data)


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['name', 'catchPhrase', 'bs']

class UserSerializer(serializers.ModelSerializer):
  address = AddressSerializer()
  company = CompanySerializer()

  class Meta:
    model = User
    fields = '__all__'

  def create(self, validated_data):
    address_data = validated_data.pop('address')
    company_data = validated_data.pop('company')

    address_instance = AddressSerializer().create(address_data)
    company_instance = Company.objects.create(**company_data)

    return User.objects.create(address=address_instance, company=company_instance, **validated_data)
  
  def update(self, instance, validated_data):
    # Update for address serializer
    address_serializer = self.fields['address']
    address_instance = instance.address 

    address_data = validated_data.pop('address')
    address_serializer.update(address_instance, address_data)

    # Update for company serializer
    company_serializer = self.fields['company']
    company_instance = instance.company

    company_data = validated_data.pop('company')
    company_serializer.update(company_instance, company_data)
    
    return super(UserSerializer, self).update(instance, validated_data)
  