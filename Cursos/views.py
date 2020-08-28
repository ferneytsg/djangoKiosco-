import os
from random import randint
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .serializers import *
import requests
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from Cursos.utils import coursesList
from Cursos.utils import authentication
from Cursos.utils import createMessageCliente
from Cursos.utils import createAssignments, upload_file
from uploadapp.models import File
from uploadapp.serializers import FileSerializer
from datetime import date
from datetime import datetime
import base64
from django.db.models import F


class UsuariosLMSViewsets(viewsets.ModelViewSet):
    queryset = UserLMS.objects.all()
    serializer_class = UserLMSSerializers


class VersionesViewsets(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionesSerializers

    def create(self, request, *args, **kwargs):

        serializer = VersionesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                versiones = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EstudiantesViewsets(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializers


class DispositivosViewsets(viewsets.ModelViewSet):
    queryset = Dispositivos.objects.all()
    serializer_class = DispositivosSerializers

    def create(self, request, *args, **kwargs):
        serializer = DispositivosSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):

            try:
                dispositivo = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def mac(self, request, pk=None):

        try:
            queryset = Dispositivos.objects.filter(MAC=pk)
            serializer_class = DispositivosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProfesoresViewsets(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializers

    def pre_save(self, obj):
        obj.samplesheet = self.request.FILES.get('file')


class GradosViewsets(viewsets.ModelViewSet):
    queryset = Grados.objects.all()
    serializer_class = GradosSerializers
    parser_classes = (MultiPartParser, JSONParser,)


class MateriasViewsets(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializers

    @action(methods=['get'], detail=True)
    def curso(self, request, pk=None):

        try:
            queryset = Materias.objects.filter(curso=pk)
            serializer_class = MateriasSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TareasViewsets(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializers

    def create(self, request, *args, **kwargs):

        serializer = TareasSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                dispositivo = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Tareas.objects.filter(materias=pk)
            serializer_class = TareasSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EvaluacionesViewsets(viewsets.ModelViewSet):
    queryset = Evaluaciones.objects.all()
    serializer_class = EvaluacionesSerializers

    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Evaluaciones.objects.filter(materias=pk)
            serializer_class = EvaluacionesSerializers(
                queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EntregasViewsets(viewsets.ModelViewSet):
    queryset = Entregas.objects.all()
    serializer_class = EntregasSerializers


class EjerciciosViewsets(viewsets.ModelViewSet):
    queryset = Ejercicios.objects.all()
    serializer_class = EjerciciosSerializers

    @action(methods=['get'], detail=True)
    def clases(self, request, pk=None):
        print(pk)
        try:
            queryset = Ejercicios.objects.filter(clases=pk)
            serializer_class = EjerciciosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PlaneacionViewsets(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionesSerializers


class MaterialEstudioViewsets(viewsets.ModelViewSet):
    queryset = MaterialEstudio.objects.all()
    serializer_class = MaterialEstudioSerializers

    @action(methods=['get'], detail=True)
    def clases(self, request, pk=None):
        print(pk)
        try:
            queryset = MaterialEstudio.objects.filter(clases=pk)
            serializer_class = MaterialEstudioSerializers(
                queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def blobmaterialestudio(self, request, pk=None):
        try:
            queryset = MaterialEstudio.objects.filter(blob__codigo=pk)

            serializer_class = MaterialEstudioSerializers(
                queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ClasesViewsets(viewsets.ModelViewSet):
    queryset = Clases.objects.all()
    serializer_class = ClasesSerializers

    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Clases.objects.filter(materias=pk)

            serializer_class = ClasesSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SubidasViewsets(viewsets.ModelViewSet):
    queryset = Subidas.objects.all()
    serializer_class = SubidasSerializers



class sincronizar():
    
    token = ''
    estudiante = ''
    session = None
    headers = None
    
    def authentication(self,username, password,estudiante):
       
        urlLogin = 'https://tsgprueba.brightspacedemo.com/d2l/lp/auth/login/login.d2l'
        
        bodyLogin = {
            "loginPath": "/d2l/login",
            "userName": username,
            "password": password
        }
        
        sincronizar.estudiante = estudiante
        sincronizar.session = requests.Session()
        
        rLogin = sincronizar.session.post(urlLogin, data=bodyLogin)
        responseLogin = rLogin.text

        csrf_token = ""
        
        counter = 0
        for data in responseLogin:
            counter += 1
            if counter >= 4214 and counter <= 4245:
                csrf_token += data

        headers = {
            'Host': 'tsgprueba.brightspacedemo.com',
            'content-type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Csrf-Token': csrf_token,
        }

        urlAuth = 'https://tsgprueba.brightspacedemo.com/d2l/lp/auth/oauth2/token'

        bodyAuth = { 'scope': '*:*:*' }
        
        rAuth = sincronizar.session.post(urlAuth, data=bodyAuth, headers=headers)

        responseAuth = rAuth.json()

        sincronizar.token = responseAuth['access_token']
        sincronizar.headers = {'Authorization': 'Bearer ' + sincronizar.token }
        
    
    def upload_file(self, idCourse, nameFile, folderFile, idFolder):
        
        file = folderFile + nameFile 
        
        # print('\n******************  Archivo en Base 64  *******************************')
        # print(type(base64.b64encode(open(file,'rb').read())))
        # print(base64.b64encode(open(file,'rb').read()))
        
        
        # print('\n******************  Archivo en bytes Hexadecimal  *******************************')
        # print(type(open(file,'rb').read()))
        # print(open(file,'rb').read())
        
        datos = base64.b64encode(open(file,'rb').read())
        
        headers = { 
                   'Authorization': 'Bearer ' + sincronizar.token,
                   'Content-type': 'multipart/mixed; boundary=xxBOUNDARYxx',
                   'Content-Disposition': 'form-data; name=""; filename="angular.jpg"'
                   }
        
        url = 'https://tsgprueba.brightspacedemo.com/d2l/api/le/1.34/'+idCourse+'/dropbox/folders/'+idFolder+'/submissions/mysubmissions/'
                    
        payload = "\
                --xxBOUNDARYxx\r\n\
                Content-Type: application/json\r\n\r\n\
                    \
                    \
                {\"Text\":\" Entrega "+nameFile+"\", \"Html\":null}\r\n--xxBOUNDARYxx\r\n\
                Content-Disposition: form-data; name=\"\"; filename=\""+nameFile+"\"\r\n\
                Content-Type: image/png\r\n\r\n\
                    \
                {"+str(datos)+"}\r\n--xxBOUNDARYxx--"
                

        
        r = sincronizar.session.post(url, data= payload, headers=headers)
        
        # print('\n')
        print('Se cargo exitosamente el archivo "'+ nameFile + '" en el folder "'+idFolder+'" del curso "'+idCourse+'"') if r.status_code == 200 else print("Error")

    
    def upload_file_to_activity(self):
        
        print("\nSubiendo archivos.....\n")
        
        activities_to_load = []
        querysetFiles = File.objects.filter(entrega__upp=0).values('codigo').annotate( 
                        nameFile=F('file'), idFolderActivity=F('entrega__tarea__codigo'), idCourse=F('entrega__tarea__materias__codigo'))       
        # print(querysetFiles)

        for data in querysetFiles:

            activities_to_load.append({"idCourse": data["idCourse"], "nameFile": data["nameFile"], "idFolderActivity": data["idFolderActivity"]})
    

        for activity in activities_to_load:
            
            Entregas.objects.filter(tarea__codigo=activity['idFolderActivity'],upp=0).update(upp=1)

            # print(activity["idCourse"], activity['nameFile'], "<p>" + activity['nameFile'] + "</p>", "./media/", activity['idFolderActivity'])
    
            self.upload_file(activity["idCourse"], activity['nameFile'], "./media/", activity['idFolderActivity'])
        


    def download_file(self, url, folder_name):
    
        local_filename = url.split('/')[-1]
        local_filename = local_filename.split("?")[0]
        path = os.path.join("./{}/{}".format(folder_name, local_filename))
        r = sincronizar.session.get(url, headers=sincronizar.headers, allow_redirects=True)
        open(path, 'wb').write(r.content)

        return local_filename


    def download_Activities(self, id1, folders):
        
        versions = Versiones.objects.all().values()

        for folder in folders:
            
            queryTareas=Tareas.objects.filter(codigo=folder) 
            if len(queryTareas) == 0:
            

                subidas = Subidas(fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                subidas.save()

                url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.assignments.api.brightspace.com/' + id1 + '/folders/' + folder
                r = requests.get(url, headers=sincronizar.headers)
                response = r.json()
                
                urlDownload = response['entities'][1]['entities'][0]['links'][1]['href']
                
                # print(response['properties']['name'], response['properties']['instructions'], response['properties']['instructionsText'], response['properties']['dueDate'])

                for j in versions:
                    j['numero'] = j['numero'] + 0.1
                    Versiones.objects.all().update(numero=j['numero'])
                    
                    
                def random_with_N_digits(n):
                    range_start = 10 ** (n - 1)
                    range_end = (10 ** n) - 1
                    return randint(range_start, range_end)

                i = 1
                while i > 0:
                    codeFile = random_with_N_digits(6)
                    ListFiles = File.objects.filter(codigo=codeFile)

                    if  len(ListFiles)==0:
                        file = File(codigo=random_with_N_digits(6), subida_id=subidas.pk, file=self.download_file(urlDownload, "media"))
                        file.save()
                        i=-2

                course = Materias.objects.filter(codigo=id1).values()
                newHomework = Tareas(nombre=response['properties']['name'], subida_id=subidas.pk, materias_id=course[0]["id"], codigo=folder)
                newHomework.save()



    def getActivity(self, id1):
        
        url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.activities.api.brightspace.com/activityusages/' + id1
        r = requests.get(url, headers=sincronizar.headers)
        response = r.json()

        urlsActivities = []
        try:
            
            for data in range(len(response['entities'])):
                urlsActivities.append(response['entities'][data]['links'][9]['href'])
                       
            idsFolders = []
            for urlActivity in urlsActivities: 
                idFolder = urlActivity.split('/')[len(urlActivity.split('/'))-1]
                idsFolders.append(idFolder)

            print("El curso "+ str(id1) +" tiene las siguientes actividades "+str(idsFolders))
        except:
            print('EL curso ' + id1 + ' no tiene actividades')

        if len(urlsActivities) != 0:
            self.download_Activities(id1, idsFolders)


    def getnewCourses(self):
        
        url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'

        r = requests.get(url, headers=sincronizar.headers)
        response = r.json()
        
        urlCourses = []
        for data in response["entities"]:
            if data["class"][2] == "course-offering":
                urlCourses.append(data["href"])

        idCourses = []
        for urlCourse in urlCourses:
            
            idCourse = urlCourse.split('/')[len(urlCourse.split('/'))-1]
            idCourses.append(idCourse)
            
        addCourses = []
        try:
            
            for id2 in idCourses:
                
                url2 = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/' + id2
                r2 = requests.get(url2, headers=sincronizar.headers)
                response2 = r2.json()
                
                r3 = requests.get(response2["entities"][2]["href"], headers=sincronizar.headers)
                responseImages = r3.json()
                urlImages = responseImages["links"][2]["href"]

                def get_as_base64(url):
                    return base64.b64encode(requests.get(url).content)
                
                materias = Materias.objects.filter(codigo=id2).exists()
                if materias is False:
                    addCourses.append({"id": id2, "name": response2["properties"]["name"], "images": get_as_base64(urlImages)})
                else:
                    self.getActivity(id2)
                    
        except Exception:
            print(Exception)
            
        for newCourse in addCourses:
            course = Materias(codigo=newCourse["id"], titulo=newCourse["name"], imagen=newCourse["images"], profesor_id=1, curso_id=1)
            course.save()
            self.getActivity(newCourse["id"])


def asignard2l():

    print("\nEmpezando sincronizacion...\n")
    querysetEstudiantes = UserLMS.objects.all().values()
    for codigo in querysetEstudiantes:
        a = sincronizar()
        a.authentication(codigo["username"], codigo["password"], codigo["estudiante_id"])
        a.getnewCourses()
        a.upload_file_to_activity()
        print('\n')



class Sincronizacion(viewsets.ModelViewSet):
    queryset = UserLMS.objects.all()
    serializer_class = UserLMSSerializers
    print("Para sincronizar abre el siguiente link http://127.0.0.1:8000/api/gobernacion/cursos/Sincronizacion/sincronizacion/ \n")

    @action(methods=['get'], detail=False)
    def sincronizacion(self, request, pk=None):
        try:
            asignard2l()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)