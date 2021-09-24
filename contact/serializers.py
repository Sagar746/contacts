from rest_framework import serializers


from .models import Contact,Email

from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['id','username','password']






class EmailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Email
		fields=['id','email']

class ContactSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	emails=EmailSerializer(many=True)
	class Meta:
		model=Contact
		fields=['id','first_name','last_name','address','label','emails']


	def create(self,validated_data):
		emails=validated_data.pop('emails')
		contacts=Contact.objects.create(**validated_data)
		for email in emails:
			Email.objects.create(contacts=contacts,**email)
		return contact

