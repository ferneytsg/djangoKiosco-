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
from Cursos.utils import createAssignments
from uploadapp.models import File
from uploadapp.serializers import FileSerializer


class UsuariosLMSViewsets(viewsets.ModelViewSet):
    queryset = UserLMS.objects.all()
    serializer_class = UserLMSSerializers


    @action(methods=['get'], detail=True)
    def media(self, request, pk=None):
        diccionario = []

        querysetMaterias = Materias.objects.all().values()
        for codigo in querysetMaterias:
            querysetfiles = File.objects.filter(
                entrega__tarea__materias__codigo=codigo["codigo"]).values()

            for data in querysetfiles:
                print(data["file"])

                diccionario.append(
                    {"codigo_curso": codigo["codigo"], "archivo": data["file"]})

        print(diccionario)
        # print(querysetfiles)

        try:
            queryset = File.objects.filter(entrega__tarea__materias__codigo=pk)
            serializer_class = FileSerializer(queryset, many=True).data
            # print(serializer_class)
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class VersionesViewsets(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionesSerializers
    # print(queryset)

    def create(self, request, *args, **kwargs):
        print(type(request.data['numero']))

        # request.data._mutable = True

        # request.data._mutable = False

        serializer = VersionesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                versiones = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    """
    def create(self, request, *args, **kwargs):
        response = requests.get('https://restcountries.eu/rest/v2/lang/es')
        ejemplo = response.json(*args, **kwargs)
        print((response.json()))

        serializer = VersionesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("ferney")
            try:
                version = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    """


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
            serializer_class = DispositivosSerializers(
                queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    """
    @action(methods=['get'], detail=True)
    def mac(self, request,pk= None):

        app_creds = {'app_id': 'G9nUpvbZQyiPrk3um2YAkQ',
            'app_key': 'ybZu7fm_JKJTFwKEHfoZ7Q'}
        ac = d2lauth.fashion_app_context(
            app_id=app_creds['app_id'], app_key=app_creds['app_key'])
        redirect_url = 'http://localhost:8080?x_a=dC31ncmeHGvtullmp-6xSu&x_b=GPo8Rm7ou1fxZ7D8JHKOu1&x_c=093VuH_tHn1WGlla7pQ7MvGDJUX8lZ5gS5jwOgR8xNE'
        uc = ac.create_user_context(
            result_uri=redirect_url, host='devcop.brightspace.com', encrypt_requests=True)
        route = '/d2l/api/versions/'
        url = uc.create_authenticated_url(route)
        url
        'https://devcop.brightspace.com/d2l/api/versions/?x_t=1338916317&x_d=lz2D5RD9LFejpriJTcw7QD8FaBPymmWpK0_mdNt5on0&x_b=dC31ncmeHGvtullmp-6xSu&x_c=pRir1VlN73yhAytcLq6kQ4krBv563YoASnKcJSwdBBY&x_a=G9nUpvbZQyiPrk3um2YAkQ'
        r = requests.get(url)
        r.status_code
        print(r.status_code)

        try:
            queryset = Dispositivos.objects.filter(MAC=pk)
            serializer_class = DispositivosSerializers(queryset,many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

"""


"""
    def create(self, request, *args, **kwargs):

        response = requests.get('https://restcountries.eu/rest/v2/lang/es')
        ejemplo = response.json(*args, **kwargs)
        print(len(ejemplo))

        for i in ejemplo:
            serializer = DispositivosSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                request.data._mutable = True
                request.data['MAC'] = i["name"]
                dispositivo = serializer.save()
                request.data._mutable = False
        return Response(serializer.data, status=status.HTTP_200_OK)
"""


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

    @action(methods=['get'], detail=False)
    def asignacion(self, request, pk=None):
        querysetArchivos = File.objects.all().values()

        print(querysetArchivos)
        for i in querysetArchivos:
            queryset = Materias.objects.filter(codigo=pk).values()
            createAssignments(pk, "Tarea react urgente", "<p>LLevar codigo</p>",
                              "2020-07-29T04:59:00.000Z", "el_artde_la_guerra.pdf", "./media/")

        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def mensaje(self, request, pk=None):

        diccionario = []
        querysetMaterias = Materias.objects.all().values()
        for codigo in querysetMaterias:

            querysetfiles = File.objects.filter(
                entrega__tarea__materias__codigo=codigo["codigo"]).values()
            print(codigo["codigo"])
            for  data in querysetfiles:
                print(data["file"])
                diccionario.append({"codigoCurso": codigo["codigo"], "nombreArchivo": data["file"]})

        print(diccionario)
        for datos in diccionario:
            print(datos)
            createMessageCliente(
                datos["codigoCurso"], datos['nombreArchivo'], "<p>" + datos['nombreArchivo'] + "</p>", "./media/")

        return Response(status=status.HTTP_200_OK)



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
            print("ferney")
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

# *******************************************************




class sincronizar():
    token = ''
    estudiante=""
    session = None
    def authentication(self,username, password,estudiante):
        # ***     creaci+on de curso  ******
        url = 'https://tsgprueba.brightspacedemo.com/d2l/lp/auth/login/login.d2l'
        sincronizar.estudiante=estudiante
        body = {
            "loginPath": "/d2l/login",
            "userName": username,
            "password": password
        }

        session = requests.Session()
        sincronizar.session = session
        r = session.post(url, data=body)
        response = r.text

        cookies = session.cookies.get_dict()

        csrftoken = ""
        counter = 0
        for data in response:
            counter += 1
            if counter >= 4214 and counter <= 4245:
                csrftoken += data

        headers = {
            'Host': 'tsgprueba.brightspacedemo.com',
            'content-type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Csrf-Token': csrftoken,
        }

        url2 = 'https://tsgprueba.brightspacedemo.com/d2l/lp/auth/oauth2/token'

        body2 = {
            'scope': '*:*:*',
        }

        r2 = requests.post(url2, data=body2, headers=headers, cookies=cookies)

        response2 = r2.json()

        sincronizar.token = response2['access_token']

    def print(self):
        print(sincronizar.token)
        print("Estudiante")
        print(sincronizar.estudiante)


    def subirmensaje(self):
        diccionario = []
        querysetMaterias = Materias.objects.all().values()
        for codigo in querysetMaterias:

            querysetfiles = File.objects.filter(
                entrega__tarea__materias__codigo=codigo["codigo"]).values()
            print(codigo["codigo"])
            for data in querysetfiles:
                print(data["file"])
                diccionario.append({"codigoCurso": codigo["codigo"], "nombreArchivo": data["file"]})

        print(diccionario)
        for datos in diccionario:
            print(datos)
            createMessageCliente(
                datos["codigoCurso"], datos['nombreArchivo'], "<p>" + datos['nombreArchivo'] + "</p>", "./media/")

    def download_file(self, url, folder_name):
        headers = {'Authorization': 'Bearer ' +
                                    sincronizar.token}
        local_filename = url.split('/')[-1]
        local_filename = local_filename.split("?")[0]
        path = os.path.join("./{}/{}".format(folder_name, local_filename))
        r = sincronizar.session.get(url, headers=headers, allow_redirects=True)
        open(path, 'wb').write(r.content)

        return local_filename





    def activities(self, id1, folders):
        headers = {'Authorization': 'Bearer ' + sincronizar.token}
        for folder in folders:
            subidas = Subidas(fecha="2020-08-12")
            subidas.save()
            #print(subidas.pk)

            url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.assignments.api.brightspace.com/' + \
                  id1 + '/folders/' + folder
            r = requests.get(url, headers=headers)
            response = r.json()
            # print('*********')
            # print(response)
            urlDownload = response['entities'][2]['entities'][0]['links'][1][
                'href']
            urlName = response['entities'][2]['entities'][0]['links'][0][
                'href']
            print("URL NAME")
            print(urlName)
            print('********************')
            name = response['properties']['name']
            title = response['properties']['instructions']
            instruction = response['properties']['instructionsText']
            date = response['properties']['dueDate']
            #print("Curso " + str(id1))
            #print(name, title, instruction, date)
            #print(urlDownload)
            #print('\n')
            versiones = Versiones.objects.all().values()

            listaActividades=File.objects.filter(file=self.download_file(urlDownload, "media"))
            if listaActividades !=0:
                print(listaActividades)
                print("Ya  existe")
            else:
                print(self.download_file(urlDownload, "media"))
                print("No existe")


            for j in versiones:
                j['numero'] = j['numero'] + 0.1
                Versiones.objects.all().update(numero=j['numero'])




            def random_with_N_digits(n):
                range_start = 10 ** (n - 1)
                range_end = (10 ** n) - 1
                return randint(range_start, range_end)

            i = 1
            while i > 0:
                codigoFile = random_with_N_digits(6)
                ListaFiles = File.objects.filter(codigo=codigoFile)

                if  len(ListaFiles)==0:
                    archivo = File(codigo=random_with_N_digits(6), subida_id=subidas.pk,
                                   file=self.download_file(urlDownload, "media")  )
                    archivo.save()
                    i=-2



            materias = Materias.objects.filter(codigo=id1).values()
            nuevaTarea = Tareas(nombre=name, subida_id=subidas.pk,materias_id=materias[0]["id"])
            nuevaTarea.save()





    def getActivity(self, id1):
        headers = {'Authorization': 'Bearer ' + sincronizar.token}
        url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.activities.api.brightspace.com/activityusages/' + id1
        r = requests.get(url, headers=headers)
        response = r.json()

        idActivities = []
        try:
            for data in range(len(response['entities'])):
                idActivities.append(
                    response['entities'][data]['links'][11]['href'])
            identificator = ""
            idsFolders = []
            for data in idActivities:
                for i in reversed(data):
                    if i == '/':
                        break
                    identificator = i + identificator
                    if len(identificator) == 3:
                        idsFolders.append(identificator)
                        identificator = ""
            # print(id1)
            # print(idsFolders)
            # print(idActivities)
        except:
            print('EL curso ' + id1 + ' no tiene actividades')

        if len(idActivities) != 0:
            self.activities(id1, idsFolders)

    def getnewCourses(self):
        headers = {'Authorization': 'Bearer ' +
                   sincronizar.token}
        # *******      Headers  ****************
        url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'

        r = requests.get(url, headers=headers)
        response = r.json()
        urlsCursos = []
        for data in response["entities"]:
            if data["class"][2] == "course-offering":
                urlsCursos.append(data["href"])

        cursos = ""
        idsCursos = []
        for urlCursos in urlsCursos:
            for i in reversed(urlCursos):
                if i == '/':
                    break
                cursos = i + cursos
                if len(cursos) == 4:
                    idsCursos.append(cursos)
                    cursos = ""
        diccionario = []
        try:
            for id2 in idsCursos:
                url2 = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/' + id2
                r2 = requests.get(url2, headers=headers)
                response2 = r2.json()
                r3 = requests.get(
                    response2["entities"][2]["href"], headers=headers)
                responseImages = r3.json()
                urlImages = responseImages["links"][2]["href"]

                def get_as_base64(url):
                    return base64.b64encode(requests.get(url).content)
                materias = Materias.objects.filter(codigo=id2).exists()
                x = response2["links"][0]["href"].split("/")
                if materias is False:
                    diccionario.append(
                        {"id": id2, "name": response2["properties"]["name"], "images": get_as_base64(urlImages)})
                else:
                    self.getActivity(id2)
        except Exception:
            print(Exception)
        for i in diccionario:
            materia = Materias(
                codigo=i["id"], titulo=i["name"], imagen=i["images"], profesor_id=1, curso_id=1)
            materia.save()
            self.getActivity(i["id"])







def crearMateria():
    try:
        for i in coursesList():
            materia = Materias(
                codigo=i["id"], titulo=i["name"], imagen=i["images"])
            materia.save()
            print(materia)
    except Exception:
        print("Estas materias ya existen")


def mensajes():
    # querysetArchivos = File.objects.all().values()

    materias = Materias.objects.all().values()
    print(materias)

    for curso in materias:
        queryset = Materias.objects.filter(codigo=curso["id"]).values()
        createAssignments(curso["codigo"], "Tarea react urgente", "<p>LLevar codigo</p>", "2020-07-29T04:59:00.000Z",
                          "el_artde_la_guerra.pdf", "./media/")


# mensajes()
# crearMateria()


def asignard2l():

    print("Asignar d2l")
    querysetEstudiantes = UserLMS.objects.all().values()
    for codigo in querysetEstudiantes:
        a = sincronizar()
        a.authentication(codigo["username"],
                         codigo["password"], codigo["estudiante_id"])
        a.getnewCourses()
        a.subirmensaje()
        # a.print()


#asignard2l()


def asignacion(self, request, pk=None):
    querysetArchivos = File.objects.all().values()

    print(querysetArchivos)
    for i in querysetArchivos:
        queryset = Materias.objects.filter(codigo=pk).values()

    return Response(status=status.HTTP_200_OK)


def principal():
    crearMateria()
    mensajes()
    asignard2l()


class Sincronizacion(viewsets.ModelViewSet):
    queryset = UserLMS.objects.all()
    serializer_class = UserLMSSerializers
    print("Hola")

    @action(methods=['get'], detail=False)
    def sincronizacion(self, request, pk=None):
        try:
            asignard2l()
            print("Hola Mundo")
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)





