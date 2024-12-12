from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class ActiveEmployeesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        active_users = User.objects.filter(is_active=True)
        serializer = UserSerializer(active_users, many=True)
        return Response(serializer.data)


