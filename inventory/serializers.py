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

# --------------IMAGE------------------------------------------
class crewNeckImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = crewNeckImg
        fields = '__all__'

class DropCutImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCutImg
        fields = '__all__'

class OversizedImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCutImg
        fields = '__all__'
# ---------------------MEN------------------------------------------------------
class OversizedMenSerializer(serializers.ModelSerializer):
    images=OversizedImgSerializer(many=True)
    class Meta:
        model = OversizedMen
        fields = '__all__'

class DropCutMenSerializer(serializers.ModelSerializer):
    images=DropCutImgSerializer(many=True)
    class Meta:
        model = DropCutMen
        fields = '__all__'

class crewNeckMenSerializer(serializers.ModelSerializer):
    images=crewNeckImgSerializer(many=True)
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
    images=OversizedImgSerializer(many=True)
    class Meta:
        model = OversizedWomen
        fields = '__all__'

class DropCutWomenSerializer(serializers.ModelSerializer):
    images=DropCutImgSerializer(many=True)
    class Meta:
        model = DropCutWomen
        fields = '__all__'

class crewNeckWomenSerializer(serializers.ModelSerializer):
    images=crewNeckImgSerializer(many=True)
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
# ---------------------------------------------------------------------------------
#-----------------------------------------MAIN----------------------------------------
class mainSerializer(serializers.ModelSerializer):
    Men = MenSerializer(many=True)
    women=womenSerializer(many=True)

    class Meta:
        model = main
        fields =['Color_name','Color_code','Themes','Men','women']
# ---------------------------------------------------------------------------------