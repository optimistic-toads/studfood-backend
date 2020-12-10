from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class UserApi(APIView):

    def get(self, request, *args, **kwargs):
        snippets = User.objects.filter(pk=request.user.pk).all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk).first()
        serializer = UserSerializer(user.first_name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
