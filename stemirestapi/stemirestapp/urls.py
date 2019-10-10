from django.conf.urls import url
from django.urls import path
from . import views

from .views import ListCaseTypeView, ListCaseTypeDetailView, CreateCaseType, \
    CreateCaseTypeDetail, FileUploadView, ListHospitalView, CreateHospital

urlpatterns = [
    path('casetype/', ListCaseTypeView.as_view(), name="casetype-all"),
    path('casetypedetail/', ListCaseTypeDetailView.as_view(), name="casetypedetails-all"),
    path('createcasetype/', CreateCaseType.as_view(), name="create"),
    path('createcasetypedetail/', CreateCaseTypeDetail.as_view(), name="create"),
    path('upload/', FileUploadView.as_view(), name="upload"),
    path('hospital/', ListHospitalView.as_view(), name="casetype-all"),
    path('hospitaldetail/', CreateHospital.as_view(), name="casetypedetails-all"),
    # path('createcasetype/', CreateCaseType.get_post_casetype,name='get_post_casetype')
]