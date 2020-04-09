from django.db import models
from django.conf import settings
# Create your models here.

class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_querySet(self):
        return StatusQuerySet(self.model, using=self._db)

class Status(models.Model):
    # User= models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, null = True, on_delete=models.SET_NULL)
    RequestHeader  = models.OneToOneField('RequestHeader', null=True, on_delete=models.CASCADE)
    Business   = models.OneToOneField('Business', null=True, on_delete=models.CASCADE)
    #Owners = models.ManyToManyField('Owner')
    CFApplicationData = models.OneToOneField('CFApplicationData', on_delete=models.CASCADE)
    objects = StatusManager()

class RequestHeader(models.Model):
    CFRequestId= models.CharField(null=True, blank=True, max_length=120)
    RequestDate = models.DateTimeField()
    CFApiUserId = models.CharField(null=True, blank=True, max_length=120)
    CFApiPassword = models.CharField(null=True, blank=True, max_length=20)
    IsTestLead= models.BooleanField(default=True)

class CFApplicationData(models.Model):
    RequestedLoanAmount= models.CharField(null=True, blank=True, max_length=120)
    StatedCreditHistory= models.IntegerField()
    LegalEntityType   = models.CharField(max_length=20)
    FilterID    = models.CharField(null=True, blank=True, max_length=120)

class Business(models.Model):
    Name    = models.CharField(max_length=20)
    SelfReportedCashFlow   = models.OneToOneField('SelfReportedCashFlow', on_delete=models.CASCADE)
    Address     = models.OneToOneField('Address', null = True, on_delete=models.CASCADE)
    TaxID   = models.CharField(null=True, blank=True, max_length=120)
    Phone    = models.CharField(null=True, blank=True, max_length=120)
    NAICS   = models.CharField(null=True, blank=True, max_length=120)
    HasBeenProfitable   = models.BooleanField(null=True)
    HasBankruptedInLast7Years = models.BooleanField(null=True)
    InceptionDate  = models.DateTimeField()


class SelfReportedCashFlow(models.Model):
    AnnualRevenue =  models.DecimalField(max_digits=20, decimal_places=2)
    MonthlyAverageBankBalance  =  models.DecimalField(max_digits=20, decimal_places=2)
    MonthlyAverageCreditCardVolume =  models.DecimalField(max_digits=20, decimal_places=2)

class Owner(models.Model):
    status= models.ForeignKey(Status, related_name='Owners', null=True, on_delete=models.CASCADE)
    Name= models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    HomeAddress = models.OneToOneField('Address', on_delete=models.CASCADE)
    DateOfBirth = models.DateTimeField()
    HomePhone = models.CharField(null=True, blank=True, max_length=120)
    SSN = models.IntegerField()
    PercentageOfOwnership= models.DecimalField(max_digits=10, decimal_places=2)

class Address(models.Model):
    Address1= models.CharField(null=True, blank=True, max_length=120)
    Address2= models.CharField(null=True, blank=True, max_length=120)
    City = models.CharField(max_length=20)
    State     = models.CharField(max_length=20)
    Zip = models.CharField(null=True, blank=True, max_length=120)
