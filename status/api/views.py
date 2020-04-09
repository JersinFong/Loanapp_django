from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response 
from .serializers import StatusSerializer

import json
from status.models import Status, RequestHeader
from django.shortcuts import get_object_or_404

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):

	permission_classes = []
	autentication_classes = []
	serializer_class = StatusSerializer
	queryset = Status.objects.all()

	def post(self, request, *args, **kwargs):
		requestId = request.data.get('RequestHeader').get('CFRequestId')
		obj = RequestHeader.objects.filter(CFRequestId = requestId)
		# if dupliate find, do update
		if(obj.count() > 0):
			status_obj = obj.first().status
			serializer = StatusSerializer(status_obj, data = request.data)
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.data)
		# else post a new one
		else:	
			return self.create(request, *args, **kwargs)


class StatusDetailAPIView(
		mixins.UpdateModelMixin,   
 		mixins.DestroyModelMixin,
 		generics.RetrieveAPIView):
	permission_classes = []
	autentication_classes = []
	queryset = Status.objects.all()
	serializer_class = StatusSerializer
	lookup_field = 'id'

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)