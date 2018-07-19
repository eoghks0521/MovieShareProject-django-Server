from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = UnicodeJSONRenderer().render(data, 'application/json; indent=4')
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST'])

def test_list(request, format=None):

    if request.method == 'GET':
        packages = TestModel.objects.all()
        serializer = TestSerializer(packages, many=True)
        return JSONResponse(serializer.data)




class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


