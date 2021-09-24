from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Contact,Email
from .serializers import ContactSerializer,EmailSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer


class ContactViewSet(ModelViewSet):
	queryset=Contact.objects.all()
	serializer_class=ContactSerializer
	authentication_classes=[TokenAuthentication]
	permission_classes=[IsAuthenticated]

class EmailViewSet(ModelViewSet):
	queryset=Email.objects.all()
	serializer_class=EmailSerializer