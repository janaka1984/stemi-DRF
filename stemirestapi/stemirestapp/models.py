from django.db import models

class CaseType(models.Model):

        HospitalId = models.CharField(max_length=50, null=False);

        RoleId = models.CharField(max_length=50, null=False);

        CaseTypeId = models.CharField(max_length=50, null=False);

        CaseTypeName = models.CharField(max_length=50, null=False);

        Source = models.CharField(max_length=50, null=False);

        Destination = models.CharField(max_length=50, null=False);

        CreatedDateTime = models.DateTimeField(max_length=50, null=False);

        class Meta:
            db_table = "CaseType"
            verbose_name = "CaseType"
            verbose_name_plural = "CaseTypes"

        def __unicode__(self):
            return self.casetypeid



class CaseTypeDetail(models.Model):

        HospitalId = models.CharField(max_length=50, null=False);

        RoleId = models.CharField(max_length=50, null=False);

        CaseTypeDetailId = models.CharField(max_length=50, null=False);

        CaseTypeDetailName = models.CharField(max_length=50, null=False);

        DisplayMsg = models.CharField(max_length=250, null=False);

        DisplaySubMsg = models.CharField(max_length=250, null=True);

        FilePath = models.CharField(max_length=250, null=True);

        IsPlaying= models.BooleanField(max_length=4, null=False);

        #File = models.FileField(max_length=1000, null=True)
        File = models.FileField(blank=False, null=True)

        BLOBFile = models.BinaryField(blank=False, null=False)

        CreatedDateTime = models.DateTimeField(max_length=50, null=False);

        class Meta:
            db_table = "CaseTypeDetail"
            verbose_name = "CaseTypeDetail"
            verbose_name_plural = "CaseTypeDetails"

        def __unicode__(self):
            return self.casetypeid

class File(models.Model):
    File = models.FileField(blank=False, null=False)

    class Meta:
        db_table = "File"

    def __str__(self):
        return self.file.name

class Hospital(models.Model):
    HospitalId = models.CharField(max_length=50, null=False);

    HospitalName = models.CharField(max_length=50, null=False);

    CreatedDateTime = models.DateTimeField(max_length=50, null=False);

    class Meta:
        db_table = "Hospital"
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"

    def __unicode__(self):
        return self.hospitalid