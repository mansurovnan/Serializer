from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status
from users.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)


# Create your views here.

#1

class UserListCreateView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
                        'msg': 'Product list',
                        'count':self.get_queryset().count(),
                        'products':serializer.data
                    }, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
                    'msg': 'Product created',
                    'product': serializer.data
                }, status=status.HTTP_201_CREATED)

class Userupdatedetaildelete(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, pk):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(user)

        return Response({
            'user': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )

        serializer = self.get_serializer(
            user,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'User updated',
            'user': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )
        user.delete()

        return Response({
            'msg': 'User deleted'
        }, status=status.HTTP_204_NO_CONTENT)




#2
        

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
