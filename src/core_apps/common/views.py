from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny


class HealthCheck(APIView):
    "API for Healthcheck of Movio Auth Service."

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        """Healthcheck for Movio Auth Service"""

        return Response({"status": "OK"}, HTTP_200_OK)
