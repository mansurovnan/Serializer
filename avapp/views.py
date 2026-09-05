from django.shortcuts import render
from users.serializers import UserSerializer
from users.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class UserCreateListView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'User created',
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        search = request.query_params.get('search')
        users = User.objects.all()
        if search:
            users = users.filter(username__icontains = search)

        page = request.query_params.get('page')
        page_size = 3

        if page and page.isdigit():
            page = int(page)
            users = users[
                page_size * (page - 1):
                page_size * page
            ]
        serializer = UserSerializer(users, many=True)

        return Response({
            'msg': 'User list',
            'count': users.count(),
            'users': serializer.data
        }, status=status.HTTP_200_OK)


class Userdetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)

        return Response({
            'msg':' user detail',
            'user detail':serializer.data

        },
        status=status.HTTP_200_OK)
    
class Userupdate(APIView):
    def put(self, request, pk):
        user = get_object_or_404(user, pk=pk)
        serializer = UserSerializer(data=request.data, isinstance = user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg':'user updated',
            'user':serializer.data
        },
        status=status.HTTP_200_OK)

    def patch(self, request, pk):
            user = get_object_or_404(user, pk=pk)
            serializer = UserSerializer(data=request.data, isinstance = user, partial = True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
    
            return Response({
                'msg':'user updated(patch)',
                'user':serializer.data
            },
            status=status.HTTP_200_OK)
    
class Userdelete(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(user, pk=pk)
        user.delete()
                
        
        return Response({
            'msg':'user updated(patch)'
            },
                status=status.HTTP_204_NO_CONTENT)

    




         
        

        
