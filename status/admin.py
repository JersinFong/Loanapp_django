from django.contrib import admin
from .models import Status, RequestHeader, CFApplicationData, Business, SelfReportedCashFlow, Owner, Address
# Register your models here.
admin.site.register(Status)
admin.site.register(RequestHeader)
admin.site.register(CFApplicationData)
admin.site.register(Business)
admin.site.register(SelfReportedCashFlow)
admin.site.register(Owner)
admin.site.register(Address)

