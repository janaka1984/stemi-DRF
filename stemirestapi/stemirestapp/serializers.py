from rest_framework import serializers

from .models import CaseType, CaseTypeDetail, File


class CaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseType
        fields = '__all__'


class CaseTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseTypeDetail
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"