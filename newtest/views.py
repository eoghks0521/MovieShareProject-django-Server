from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from django.core.files.storage import FileSystemStorage


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data, 'application/json; indent=4')
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST'])
def test_list(request, format=None):

    if request.method == 'GET':
        packages = TestModel.objects.all()
        serializer = TestSerializer(packages, many=True)
        return JSONResponse(serializer.data)


class PassIdViewSet(viewsets.ModelViewSet):
	queryset = PassId.objects.all()
	serializer_class = PassIdSerializer


	def create(self, request, *args, **kwargs):
		print(request.data['passid'])
		response_data={"success": "1"}
		return JSONResponse(response_data)

def test(request):
	return render(request, "./newtest/index.html")


class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


def upload_file(request):
   if request.method == 'POST':
      img = request.FILES['img']
      video = request.FILES['video']
      fs = FileSystemStorage()
      #filename = fs.save(img.name, img)

      file = Media(clientid = '1', img = img, video = video)
      file.save()

   return render(request, 'newtest/index.html')