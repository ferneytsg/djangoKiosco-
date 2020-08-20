from rest_framework import  serializers
from .models import *





class VersionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Versiones
        fields = ('__all__')

class ProfesoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = ('__all__')

class GradosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grados
        fields = ('__all__')



class EstudiantesSerializers(serializers.ModelSerializer):
    curso=GradosSerializers(read_only=True)
    curso_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Grados.objects.all(), source='curso')

    class Meta:
        model = Estudiantes
        fields = ('__all__')


class UserLMSSerializers(serializers.ModelSerializer):
    estudiante = EstudiantesSerializers(read_only=True)
    estudiante_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estudiantes.objects.all(), source='estudiante')

    class Meta:
        model = UserLMS
        fields = ('__all__')

class DispositivosSerializers(serializers.ModelSerializer):
    estudiante = EstudiantesSerializers(read_only=True)
    class Meta:

        model = Dispositivos
        fields = ('__all__')

    """  curso = GradosSerializers(read_only=True)"""
class MateriasSerializers(serializers.ModelSerializer):
    curso = GradosSerializers(read_only=True)
    curso_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Grados.objects.all(), source='curso')
    profesor = ProfesoresSerializers(read_only=True)
    profesor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Profesores.objects.all(), source='profesor')

    class Meta:
        model = Materias
        fields = ('__all__')

class SubidasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subidas
        fields = ('__all__')

class TareasSerializers(serializers.ModelSerializer):
    subida=SubidasSerializers(read_only=True)
    subida_id=serializers.PrimaryKeyRelatedField(write_only=True,queryset=Subidas.objects.all(),source='subida')
    materias_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Materias.objects.all(), source='materias')

    class Meta:
        model = Tareas
        fields = ('__all__')

class EvaluacionesSerializers(serializers.ModelSerializer):
    subida = SubidasSerializers(read_only=True)
    subida_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Subidas.objects.all(), source='subida')

    class Meta:
        model = Evaluaciones
        fields = ('__all__')

class EntregasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Entregas
        fields = ('__all__')




class EjerciciosSerializers(serializers.ModelSerializer):
    subida=SubidasSerializers(read_only=True)
    subida_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Subidas.objects.all(), source='subida')


    class Meta:
        model = Ejercicios
        fields = ('__all__')

class PlaneacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Planeacion
        fields = ('__all__')


class MaterialEstudioSerializers(serializers.ModelSerializer):

    class Meta:
        model = MaterialEstudio
        fields = ('__all__')

class ClasesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clases
        fields = ('__all__')
