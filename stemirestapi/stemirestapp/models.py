from django.db import models

class CaseType(models.Model):

        casetypeid = models.CharField(max_length=50, null=False);

        casetypename = models.CharField(max_length=50, null=False);

        createddatetime = models.DateTimeField(max_length=50, null=False);

        class Meta:
            db_table = "CaseType"
            verbose_name = "CaseType"
            verbose_name_plural = "CaseTypes"

        def __unicode__(self):
            return self.casetypeid



class CaseTypeDetail(models.Model):

        casetypedetailid = models.CharField(max_length=50, null=False);

        casetypedetailname = models.CharField(max_length=50, null=False);

        displaymsg = models.CharField(max_length=250, null=False);

        displaysubmsg = models.CharField(max_length=250, null=False);

        filepath = models.CharField(max_length=250, null=True);

        isplaying= models.BooleanField(max_length=4, null=False);

        file = models.FileField(blank=False, null=True)

        createddatetime = models.DateTimeField(max_length=50, null=False);

        class Meta:
            db_table = "CaseTypeDetail"
            verbose_name = "CaseTypeDetail"
            verbose_name_plural = "CaseTypeDetails"

        def __unicode__(self):
            return self.casetypeid

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    class Meta:
        db_table = "File"

    def __str__(self):
        return self.file.name