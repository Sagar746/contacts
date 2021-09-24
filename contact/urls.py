from django.urls import path,include


from contact.views import ContactViewSet,EmailViewSet,UserViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
router.register('email', EmailViewSet, basename='email')
router.register('login',UserViewSet)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
	path('',include(router.urls)),
	path('login/',obtain_auth_token),

]