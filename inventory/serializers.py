from rest_framework import serializers
from .models import *
from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.core import serializers
from rest_framework import serializers
from urllib import request
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse

# ---------------------MEN------------------------------------------------------
class OversizedMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OversizedMen
        fields = '__all__'

class DropCutMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCutMen
        fields = '__all__'

class crewNeckMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = crewNeckMen
        fields = '__all__'

class MenSerializer(serializers.ModelSerializer):
    crew_neck = crewNeckMenSerializer(many=True)
    drop_cut = DropCutMenSerializer(many=True)
    oversized = OversizedMenSerializer(many=True)

    class Meta:
        model = men
        fields = '__all__'
#--------------------------------------------------------------------
# ----------------------WOMEN -------------------------------------------------------------------------

class OversizedWomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OversizedWomen
        fields = '__all__'

class DropCutWomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCutWomen
        fields = '__all__'

class crewNeckWomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = crewNeckWomen
        fields = '__all__'

class womenSerializer(serializers.ModelSerializer):
    crew_neck = crewNeckWomenSerializer(many=True)
    drop_cut = DropCutWomenSerializer(many=True)
    oversized = OversizedWomenSerializer(many=True)

    class Meta:
        model = men
        fields = '__all__'
# -----------------------------------------------------------------------------------------
#-----------------------------------------MAIN---------------------------------------------------
class mainSerializer(serializers.ModelSerializer):
    Men = MenSerializer(many=True)
    women=womenSerializer(many=True)

    class Meta:
        model = main
        fields =['Design_name','Design_id','Themes','Men','women']
# ---------------------------------------------------------------------------------