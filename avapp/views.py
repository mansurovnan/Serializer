from django.shortcuts import render
from users.serializers import UserSerializer
from users.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class Usercreate(APIView):
    def post(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg':'Product created',
            'product':serializer.data
        },
        status=status.HTTP_201_CREATED
        )

class UserList(APIView):
    def get(self,request):
        users = User.object.all()
        serializer = UserSerializer(User, many=True)

        return Response({
            'msg':'user list',
            'count': User.count,
            'products':serializer.data
        },
        status=status.HTTP_200_OK)

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

    




         
        

        
