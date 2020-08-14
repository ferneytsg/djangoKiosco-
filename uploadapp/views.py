from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from uploadapp.serializers import FileSerializer
from uploadapp.models import File
from rest_framework import  status
"""
class FileViewset(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        print("&&&&&&&&")
        return super(FileViewset, self).create(request,*args,**args)

    @action(methods=['POST'],detail=False)
    def upload_in_api(self,request):
        print("upload  fghjk")
        serializer= FileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                file=request.FILES['file']
                print(file)

                UploadData(file)
            except Exception as err:
                print(err.__str__())
                return Response(err.__str__(),status.HTTP_400_BAD_REQUEST)

            new_file=serializer.save()
            return Response(FileSerializer(new_file).data,status.HTTP_201_CREATED)





"""

class FileViewset(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer


    def create(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("ferney")
            try:
                file = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    parser_clas = (FileUploadParser,)
    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileView(ListAPIView):
    serializer_class = FileSerializer
    def get_queryset(self):
        return File.objects.all()
"""pruebas"""

class FileView(ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(pk=self.kwargs['pk'])


class EntregasView(ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        print(self.kwargs['pk'])
        return File.objects.filter(entrega=self.kwargs['pk'])


class SubidasView(ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        print(self.kwargs['pk'])
        return File.objects.filter(subida=self.kwargs['pk'])






""""
    def get_queryset(self):
        return super(DefaultsListView, self).get_queryset().filter(
            device_id=self.kwargs['device']
        )
"""
