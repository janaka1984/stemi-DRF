from xmlrpc.client import DateTime

from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from datetime import datetime, timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .serializers import CaseTypeSerializer, CaseTypeDetailSerializer
from .models import CaseType, CaseTypeDetail


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_casetype(casetypeid="", casetypename="", createddatetime=""):
        if casetypeid != "" and casetypename != "":
            CaseType.objects.create(casetypeid=casetypeid, casetypename=casetypename, createddatetime=createddatetime)

    @staticmethod
    def create_casetypedetail(casetypedetailid="", casetypedetailname="",displaymsg="", displaysubmsg="", filepath="", isplaying="", createddatetime="" ):
        if casetypedetailid != "" and casetypedetailname != "":
            CaseTypeDetail.objects.create(casetypedetailid=casetypedetailid, casetypedetailname=casetypedetailname,
                                          displaymsg=displaymsg, displaysubmsg=displaysubmsg, filepath=filepath, isplaying=isplaying,
                                          createddatetime=createddatetime)

    def setUp(self):
        # add test data
        self.create_casetype("Case 01", "Case - Stroke:city01",  datetime.now(tz=timezone.utc))
        self.create_casetype("Case 02", "Case - Stroke:city02",  datetime.now(tz=timezone.utc))
        self.create_casetypedetail("Case 01", "Case - Stroke:city01", "New Case aly", "yes aly", "none", 0,  datetime.now(tz=timezone.utc))
        self.create_casetypedetail("Case 01", "Case - Stroke:city02", "Is STEMI aly", "yes aly", "none", 0,  datetime.now(tz=timezone.utc))
        self.create_casetypedetail("Case 02", "Case - Stroke:city02", "New Case aly", "yes aly", "none", 0,  datetime.now(tz=timezone.utc))
        self.create_casetypedetail("Case 03", "Case - Stroke:city02", "Is STEMI aly", "yes aly", "none", 0,  datetime.now(tz=timezone.utc))


class GetAllCaseTypesTest(BaseViewTest):

       def test_get_all_casetypes(self):
           """
           This test ensures that all casetype added in the setUp method
           exist when we make a GET request to the casetype/ endpoint
           """
           # hit the API endpoint
           response = self.client.get(
               reverse("casetype-all", kwargs={"version": "v1"})
           )
           # fetch the data from db
           expected = CaseType.objects.all()
           serialized = CaseTypeSerializer(expected, many=True)
           self.assertEqual(response.data, serialized.data)

           self.assertEqual(response.status_code, status.HTTP_200_OK)

       def test_get_all_casetypedetail(self):
           """
           This test ensures that all casetype added in the setUp method
           exist when we make a GET request to the casetype/ endpoint
           """
           # hit the API endpoint
           response = self.client.get(
               reverse("casetypedetails-all", kwargs={"version": "v1"})
           )
           # fetch the data from db
           expected = CaseTypeDetail.objects.all()
           serialized = CaseTypeDetailSerializer(expected, many=True)
           self.assertEqual(response.data, serialized.data)

           self.assertEqual(response.status_code, status.HTTP_200_OK)


# class ViewTestCase(TestCase):
#     """Test suite for the api views."""
#
#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.client = APIClient()
#         self.casetype_data = {
#             "casetypeid": "case1",
#             "casetypename": "case one",
#             "createddatetime": "2019-09-12 00:09:11"
#         }
#         self.response = self.client.post(
#             reverse('get_post_casetype'),
#             self.casetype_data,
#             format="json")
#
#     def test_api_can_create_a_casetype(self):
#         """Test the api has bucket creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)