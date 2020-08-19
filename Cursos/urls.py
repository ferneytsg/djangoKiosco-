from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewsets with it.
router = DefaultRouter()


router.register('usuariosLMS', UsuariosLMSViewsets)
router.register('versiones', VersionesViewsets)
router.register('disposotivos', DispositivosViewsets)
router.register('clases', ClasesViewsets)
router.register('grados', GradosViewsets)
router.register('ejercicios', EjerciciosViewsets)
router.register('entregas', EntregasViewsets)
router.register('estudiantes', EstudiantesViewsets)
router.register('evaluaciones', EvaluacionesViewsets)
router.register('materialestudio', MaterialEstudioViewsets)
router.register('materias', MateriasViewsets)
router.register('planeacion', PlaneacionViewsets)
router.register('profesores', ProfesoresViewsets)
router.register('subidas', SubidasViewsets)
router.register('tareas', TareasViewsets)
router.register('Sincronizacion', Sincronizacion)

# The API URLs are now determined automatically by the router.
urlpatterns = [

    path('', include(router.urls)),


]
