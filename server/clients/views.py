from django.shortcuts import render
from .models import Calendario
from .tools import get_rif_of_day_report, get_report_of_rif

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(f" user:{username}, password:{password}")
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )


def EmailView(request):
    # template_name = "report.html"

    hoy = datetime.now()
    end_rif = get_rif_of_day_report(hoy)
    context = {"reports": get_report_of_rif(end_rif), "mes": hoy.month}

    # context = get_rif_of_day_report(Calendario)
    return render(request, "report.html", context)
