from django.contrib import admin

# Register your models here.
from .models import CaseType, CaseTypeDetail, File, Hospital

admin.site.register(CaseType)
admin.site.register(CaseTypeDetail)
admin.site.register(File)
admin.site.register(Hospital)

