from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from users.serializers import UserSerializerserializers
from .models import User

# Create your views here.

class UserViewSet(ViewSet):
    def create(self, request):
        pass
    def list(self, request):
        pass
    def retrive(self, request):
        pass
    def list(self, request):
        pass
    def update(self, request):
        pass
    def partial_update(self, request):
        pass
    def destroy(self, request):
        pass
