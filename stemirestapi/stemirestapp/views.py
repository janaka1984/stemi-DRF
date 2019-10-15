from django.shortcuts import render

# Create your views here.
from rest_framework import generics, request, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CaseType, CaseTypeDetail, File, Hospital
from .serializers import CaseTypeSerializer, CaseTypeDetailSerializer, FileSerializer, HospitalSerializer

# Case Type
'''class ListCaseTypeView(generics.ListAPIView):
    queryset = CaseType.objects.all()
    serializer_class = CaseTypeSerializer'''


class ListCaseTypeView(generics.ListAPIView):
    queryset = CaseType.objects.all()
    serializer_class = CaseTypeSerializer

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        queryset = CaseType.objects.all()
        hospital_id = self.request.query_params.get('hospitalid', None)
        dest = self.request.query_params.get('dest', None)
        if hospital_id is not None:
            queryset = queryset.filter(HospitalId = hospital_id, Destination = dest)

        return queryset


class CreateCaseType(generics.ListCreateAPIView):
    queryset = CaseType.objects.all()
    serializer_class = CaseTypeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new CaseType."""
        serializer.save()

    # @api_view(['GET', 'POST'])
    # def get_post_casetype(request):
    #     if request.method == 'GET':
    #         """This class defines the create behavior of our rest api."""
    #         queryset = CaseType.objects.all()
    #         serializer_class = CaseTypeSerializer
    #
    #     if request.method == 'POST':
    #         data = {
    #             "casetypeid": request.data.get("casetypeid"),
    #             "casetypename": request.data.get("casetypename"),
    #             "createddatetime":request.data.get("createddatetime")
    #         }
    #         serializer = CaseTypeSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCaseTypeDetailView(generics.ListAPIView):
    queryset = CaseTypeDetail.objects.all()
    serializer_class = CaseTypeDetailSerializer


# CaseType Detail
class CreateCaseTypeDetail(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = CaseTypeDetail.objects.all()
    serializer_class = CaseTypeDetailSerializer
    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        # serializer = FileSerializer(data=request.data)
        """Save the post data when creating a new CaseType."""
        serializer.save()


# File
class FileUploadView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Hospital
class ListHospitalView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class CreateHospital(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new CaseType."""
        serializer.save()
