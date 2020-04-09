from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Status
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
import json
# Create your tests here.
User = get_user_model()

class StatusTestCase(TestCase):
	"""docstring for StatusTestCase"""
	def setUp(self):
		user = User.objects.create(username='test', email='test@test.com')
		user.set_password("yeahhh")
		user.save()

	def test_create_user(self):
		qs = User.objects.all()
		self.assertEqual(qs.count(), 1)
		qs = User.objects.filter(username='test')
		self.assertEqual(qs.count(), 1)

	def test_status_CRUD(self):
		'''
			Test creat/POST loanapp
		'''
		self.assertEqual(Status.objects.count(), 0)
		url = api_reverse('api-status:post')
		data = {
					"RequestHeader": {
					    "CFRequestId": "500653901",
					    "RequestDate": "2019-06-26T23:05:41.2898238Z",
					    "CFApiUserId": None,
					    "CFApiPassword": None,
					    "IsTestLead": True
					  },
					  "Business": {
					    "Name": "Wow Inc",
					    "SelfReportedCashFlow": {
					      "AnnualRevenue": 49999999.0,
					      "MonthlyAverageBankBalance": 94941.0,
					      "MonthlyAverageCreditCardVolume": 18191.0
					    },
					    "Address": {
					      "Address1": "1234 Red Ln",
					      "Address2": "5678 Blue Rd",
					      "City": "Santa Monica",
					      "State": "CA",
					      "Zip": "45321"
					    },
					    "TaxID": "839674398",
					    "Phone": "6573248876",
					    "NAICS": "79232",
					    "HasBeenProfitable": True,
					    "HasBankruptedInLast7Years": False,
					    "InceptionDate": "2008-06-28T23:04:03.5507585+00:00"
					  },
					  "Owners": [
					    {
					      "Name": "WH KennyTest",
					      "FirstName": "WH",
					      "LastName": "KennyTest",
					      "Email": "whkennytest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "5567 North Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3451289776",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },
					    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    }
					  ],
					  "CFApplicationData": {
					    "RequestedLoanAmount": "49999999",
					    "StatedCreditHistory": 1,
					    "LegalEntityType": "LLC",
					    "FilterID": "897079"
					  }
				}

		response = self.client.post(url, json.dumps(data) ,content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Status.objects.count(), 1)
		data_id = response.data.get('id')

		'''
			test retrieve/GET loanapp status
		'''
		detial_url = api_reverse("api-status:detail", kwargs={"id": data_id})
		get_response = self.client.get(detial_url, content_type='application/json')
		self.assertEqual(get_response.status_code, status.HTTP_200_OK)
		self.assertEqual(Status.objects.count(), 1)

		'''
			test update/PUT loanapp status
		'''
		put_data={
					"RequestHeader": {
					    "CFRequestId": "500653901",
					    "RequestDate": "2019-06-26T23:05:41.2898238Z",
					    "CFApiUserId": None,
					    "CFApiPassword": None,
					    "IsTestLead": True
					  },
					  "Business": {
					    "Name": "USC",
					    "SelfReportedCashFlow": {
					      "AnnualRevenue": 49999999.0,
					      "MonthlyAverageBankBalance": 94941.0,
					      "MonthlyAverageCreditCardVolume": 18191.0
					    },
					    "Address": {
					      "Address1": "1234 Red Ln",
					      "Address2": "5678 Blue Rd",
					      "City": "Santa Monica",
					      "State": "CA",
					      "Zip": "45321"
					    },
					    "TaxID": "839674398",
					    "Phone": "6573248876",
					    "NAICS": "79232",
					    "HasBeenProfitable": True,
					    "HasBankruptedInLast7Years": False,
					    "InceptionDate": "2008-06-28T23:04:03.5507585+00:00"
					  },
					  "Owners": [
					    {
					      "Name": "WH KennyTest",
					      "FirstName": "WH",
					      "LastName": "KennyTest",
					      "Email": "whkennytest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "5567 North Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3451289776",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },
					    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    },    {
					      "Name": "Test DoeTest",
					      "FirstName": "Test",
					      "LastName": "DoeTest",
					      "Email": "Doetest@caminofinancial.com",
					      "HomeAddress": {
					        "Address1": "4512 East Ridge Ct",
					        "Address2": None,
					        "City": "Berkeley",
					        "State": "CA",
					        "Zip": "94704"
					      },
					      "DateOfBirth": "1955-12-18T00:00:00",
					      "HomePhone": "3107654321",
					      "SSN": "435790261",
					      "PercentageOfOwnership": 50.0
					    }
					  ],
					  "CFApplicationData": {
					    "RequestedLoanAmount": "49999999",
					    "StatedCreditHistory": 1,
					    "LegalEntityType": "LLC",
					    "FilterID": "897079"
					  }

				}

		put_response = self.client.put(detial_url, json.dumps(put_data), content_type='application/json')
		self.assertEqual(put_response.status_code, status.HTTP_200_OK)
		self.assertEqual(put_response.data["Business"]["Name"], "USC")
		self.assertEqual(Status.objects.count(), 1)

		
		'''
		test POST duplicate data
		'''
		duplicate_response = self.client.post(url, json.dumps(data) ,content_type='application/json')
		self.assertEqual(duplicate_response.status_code, status.HTTP_200_OK)
		self.assertEqual(Status.objects.count(), 1)


		'''
		test DELETE loanapp status
		'''
		delete_response = self.client.delete(detial_url, content_type='application/json')
		self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
		get_response = self.client.get(detial_url, content_type='application/json')
		self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
		self.assertEqual(Status.objects.count(), 0)
		


