from .models import Account
from rest_framework import viewsets ,generics,status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class =UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)