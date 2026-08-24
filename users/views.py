from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
def User_list_create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({

                'msg': 'User created',
                'User': serializer.data
            },
            status=status.HTTP_201_CREATED

        )

    if request.methos == 'GET':
        Users = Users.object.all()

        serializer = UserSerializer(Users, many=True)

        return Response(
            {
                'msg': 'User list',
                'count': products.count(),
                'products': serializer.data
            },
            status=status.HTTP_200_OK
        )

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, pk):

    product = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer (User)

        return Response(
            {
                'msg': 'User detail',
                'User': serializer.data
            },
            status=status.HTTP_200_OK
        )

    if request.method == 'PUT':
        serializer = UserSerializer (
            User,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'msg': 'User updated',
                'User': serializer.data
            },
            status=status.HTTP_200_OK
        )

    if request.method == 'PATCH':
        serializer = UserSerializer (
            User,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'msg': 'User partially updated',
                'User': serializer.data
            },
            status=status.HTTP_200_OK
        )

    if request.method == 'DELETE':
        User.delete()

        return Response(
            {
                'msg': 'User deleted successfully'
            },
            status=status.HTTP_200_OK
        )



