from rest_framework import serializers
from status.models import Status, RequestHeader as RH, CFApplicationData as CFA, Business as BU, SelfReportedCashFlow as SRCF, Owner as OW, Address as AD


class RequestHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RH
        fields = [
            'CFRequestId',
            'RequestDate',
            'CFApiUserId', 
            'CFApiPassword',
            'IsTestLead',
        ]
    def create(self, validated_data):
        return RH.objects.create(**validated_data)

class CFApplicationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFA
        fields = [
            'RequestedLoanAmount',
            'StatedCreditHistory',
            'LegalEntityType', 
            'FilterID',
        ]
    def create(self, validated_data):
        return CFA.objects.create(**validated_data)

class SelfReportedCashFlowSerialize(serializers.ModelSerializer):
    class Meta:
        model = SRCF
        fields = [
            'AnnualRevenue',
            'MonthlyAverageBankBalance',
            'MonthlyAverageCreditCardVolume', 
        ]
    def create(self, validated_data):
        return SRCF.objects.create(**validated_data)

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AD
        fields = [
            'Address1',
            'Address2',
            'City',
            'State',
            'Zip', 
        ]
    def create(self, validated_data):
        return AD.objects.create(**validated_data)

class BusinessSerializer(serializers.ModelSerializer):
    SelfReportedCashFlow = SelfReportedCashFlowSerialize()
    Address = AddressSerializer()
    class Meta:
        model = BU
        fields = [
            "Name",
            "SelfReportedCashFlow",
            "Address",
            "TaxID",
            "Phone",
            "NAICS",
            "HasBeenProfitable",
            "HasBankruptedInLast7Years",
            "InceptionDate", 
        ]
    def create(self, validated_data):
        Address_data = validated_data.pop('Address')
        Address_obj = AddressSerializer.create(AddressSerializer(), validated_data = Address_data)
        SelfReportedCashFlow_data = validated_data.pop('SelfReportedCashFlow')
        SelfReportedCashFlow_obj = SelfReportedCashFlowSerialize.create(SelfReportedCashFlowSerialize(), validated_data = SelfReportedCashFlow_data)
        Business_obj = BU.objects.update_or_create(
                                                Name = validated_data.pop('Name'),
        	                                    Address = Address_obj, 
                                                SelfReportedCashFlow = SelfReportedCashFlow_obj,
                                                TaxID = validated_data.pop('TaxID'),
                                                Phone = validated_data.pop('Phone'),
                                                NAICS = validated_data.pop('NAICS'),
                                                HasBeenProfitable = validated_data.pop('HasBeenProfitable'),
                                                HasBankruptedInLast7Years = validated_data.pop('HasBankruptedInLast7Years'),
                                                InceptionDate = validated_data.pop('InceptionDate'))
        return Business_obj

    def update(self, instance, validated_data):
        Address_data = validated_data.pop('Address')
        Address_obj = AddressSerializer.update(AddressSerializer(), instance.Address, validated_data = Address_data)
        SelfReportedCashFlow_data = validated_data.pop('SelfReportedCashFlow')
        SelfReportedCashFlow_obj = SelfReportedCashFlowSerialize.update(SelfReportedCashFlowSerialize(), instance.SelfReportedCashFlow, validated_data = SelfReportedCashFlow_data)
        setattr(instance, 'Name', validated_data.pop('Name'))
        setattr(instance, 'Address', Address_obj)
        setattr(instance, 'SelfReportedCashFlow', SelfReportedCashFlow_obj)
        setattr(instance, 'TaxID', validated_data.pop('TaxID'))
        setattr(instance, 'Phone', validated_data.pop('Phone'))
        setattr(instance, 'NAICS', validated_data.pop('NAICS'))
        setattr(instance, 'HasBeenProfitable', validated_data.pop('HasBeenProfitable'))
        setattr(instance, 'HasBankruptedInLast7Years', validated_data.pop('HasBankruptedInLast7Years'))
        setattr(instance, 'InceptionDate', validated_data.pop('InceptionDate'))
        instance.save()
        return instance




class OwnerSerializer(serializers.ModelSerializer):
    HomeAddress = AddressSerializer()
    class Meta:
        model = OW
        fields = [
            "Name",
            "FirstName",
            "LastName",
            "Email",
            "HomeAddress",
            "DateOfBirth",
            "HomePhone",
            "SSN",
            "PercentageOfOwnership",
        ]

    def create(self, validated_data, Status_obj):
        HomeAddress_data   = validated_data.pop('HomeAddress')
        HomeAddress_obj = AddressSerializer.create(AddressSerializer(), validated_data = HomeAddress_data) 
        Owner_obj  = OW.objects.create(
        										status = Status_obj,
        	                                    HomeAddress = HomeAddress_obj,
        	                                    Name = validated_data.pop('Name'), 
                                                FirstName = validated_data.pop('FirstName'),
                                                LastName = validated_data.pop('LastName'),
                                                Email = validated_data.pop('Email'),
                                                DateOfBirth = validated_data.pop('DateOfBirth'),
                                                HomePhone = validated_data.pop('HomePhone'),
                                                SSN = validated_data.pop('SSN'),
                                                PercentageOfOwnership = validated_data.pop('PercentageOfOwnership'))
        return Owner_obj


class StatusSerializer(serializers.ModelSerializer):
    RequestHeader = RequestHeaderSerializer()
    Owners = OwnerSerializer(many=True)
    Business = BusinessSerializer()
    CFApplicationData = CFApplicationDataSerializer()
    class Meta:
        model = Status
        fields = [
        	'id',
            'RequestHeader',
            'Business',
            'Owners',
            'CFApplicationData',
        ]

    
    def create(self, validated_data):
        RequestHeader_data = validated_data.pop('RequestHeader')
        RequestHeader_obj = RequestHeaderSerializer.create(RequestHeaderSerializer(),validated_data = RequestHeader_data)
        CFApplicationData_data = validated_data.pop('CFApplicationData')
        CFApplicationData_obj = CFApplicationDataSerializer.create(CFApplicationDataSerializer(), validated_data = CFApplicationData_data)
        Business_data = validated_data.pop('Business')
        Business_obj = BusinessSerializer.create(BusinessSerializer(), validated_data = Business_data)[0]
        Owners_data = validated_data.pop('Owners')
        Status_obj = Status.objects.create(
        	                                RequestHeader = RequestHeader_obj,
        	                                Business = Business_obj,
        	                                CFApplicationData = CFApplicationData_obj)
        for owner_data in Owners_data:
            OwnerSerializer.create(OwnerSerializer(), validated_data = owner_data, Status_obj = Status_obj)
        
        return Status_obj

    def update(self, instance, validated_data):
        RequestHeader_data = validated_data.pop('RequestHeader')
        RequestHeader_obj = RequestHeaderSerializer.update(RequestHeaderSerializer(), instance.RequestHeader ,validated_data = RequestHeader_data)
        CFApplicationData_data = validated_data.pop('CFApplicationData')
        CFApplicationData_obj = CFApplicationDataSerializer.update(CFApplicationDataSerializer(),instance.CFApplicationData ,validated_data = CFApplicationData_data)
        Business_data = validated_data.pop('Business')
        Business_obj = BusinessSerializer.update(BusinessSerializer(), instance.Business, validated_data = Business_data)
        Owners_data = validated_data.pop('Owners')
        setattr(instance, 'RequestHeader', RequestHeader_obj)
        setattr(instance, 'Business', Business_obj)
        setattr(instance, 'CFApplicationData', CFApplicationData_obj)
        instance.Owners.all().delete()
        for owner_data in Owners_data:
            OwnerSerializer.create(OwnerSerializer(), validated_data = owner_data, Status_obj = instance)
        
        instance.save()
        return instance

    



