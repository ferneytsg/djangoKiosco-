from django.db import models


class UserLMS(models.Model):
    username=models.CharField(max_length=50, null=False, blank=True)
    password=models.CharField(max_length=50, null=False, blank=True)
    estudiante = models.OneToOneField('Cursos.Estudiantes', on_delete=models.CASCADE, null=True, blank=True)


class Versiones (models.Model):
    numero = models.FloatField(null=True, blank=True, default=0.0)


class Estudiantes(models.Model):
    codigo = models.IntegerField(unique=True)
    nombres = models.CharField(max_length=50, null=False, blank=True)
    apellidos = models.CharField(max_length=50, null=False, blank=True)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey('Cursos.Grados', on_delete=models.CASCADE, null=True, blank=True)


class Dispositivos(models.Model):
    MAC = models.CharField(max_length=50, null=False, blank=True)
    estudiante = models.OneToOneField('Cursos.Estudiantes', on_delete=models.CASCADE, null=True, blank=True)


class Profesores(models.Model):
    codigo = models.IntegerField( null=False,unique=True)
    nombres = models.CharField(max_length=50, null=False, blank=True)
    apellidos = models.CharField(max_length=50, null=False, blank=True)
    fecha_nacimiento = models.DateField()


class Grados(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=True)


class Materias(models.Model):
    codigo=models.CharField(max_length=200, unique=True, null=False, blank=True)
    titulo=models.CharField(max_length=200, null=False, blank=True)
    subtitulo=models.CharField(max_length=200, null=False, blank=True)
    descripcion=models.CharField(max_length=200, null=False, blank=True)
    imagen=models.TextField( null=False, blank=True)
    curso = models.ForeignKey('Cursos.Grados', on_delete=models.CASCADE, null=True, blank=True)
    profesor = models.ForeignKey('Cursos.Profesores', on_delete=models.CASCADE, null=True, blank=True)


class Tareas(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=True)
    codigo = models.CharField(max_length=50,null=True ,blank=True)
    materias = models.ForeignKey('Cursos.Materias', on_delete=models.CASCADE, null=False, blank=True)
    subida = models.ForeignKey('Cursos.Subidas', on_delete=models.CASCADE, null=True, blank=True)
    estudiante= models.ForeignKey('Cursos.Estudiantes', on_delete=models.CASCADE, null=True, blank=True)
    


class Evaluaciones(models.Model):
    nombre=models.CharField(max_length=50,null=False,blank=True)
    materias = models.ForeignKey('Cursos.Materias', on_delete=models.CASCADE, null=True, blank=True)
    subida=models.ForeignKey('Cursos.Subidas', on_delete=models.CASCADE,null=True,blank=True)


class Entregas(models.Model):
    creado=models.DateField(auto_now=True)
    upp=models.IntegerField(default=0)
    ejercios=models.ForeignKey('Cursos.Ejercicios', on_delete=models.CASCADE,null=True,blank=True)
    tarea=subida=models.ForeignKey('Cursos.Tareas', on_delete=models.CASCADE,null=True,blank=True)
    evaluacion=models.ForeignKey('Cursos.Evaluaciones', on_delete=models.CASCADE,null=True,blank=True)
    subida=models.ForeignKey('Cursos.Subidas', on_delete=models.CASCADE,null=True,blank=True)
    estudiante= models.ForeignKey('Cursos.Estudiantes', on_delete=models.CASCADE, null=True, blank=True)


class Ejercicios(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    subida=models.ForeignKey('Cursos.Subidas', on_delete=models.CASCADE,null=True,blank=True)
    clases=models.ForeignKey('Cursos.Clases', on_delete=models.CASCADE,null=True,blank=True)


class Planeacion(models.Model):
    fecha=models.DateField()
    tarea=models.ForeignKey('Cursos.Tareas', on_delete=models.CASCADE,null=True,blank=True)
    ejercicios=models.ForeignKey('Cursos.Ejercicios', on_delete=models.CASCADE,null=True,blank=True)
    clase=models.ForeignKey('Cursos.Clases', on_delete=models.CASCADE,null=True,blank=True)
    evaluacion=models.ForeignKey('Cursos.Evaluaciones', on_delete=models.CASCADE,null=True,blank=True)


class MaterialEstudio(models.Model):
    nombre=models.CharField(max_length=50,null=False,blank=True)
    descripcion=models.CharField(max_length=255,null=False,blank=True)
    clases=models.ForeignKey('Cursos.Clases', on_delete=models.CASCADE,null=True,blank=True)
    blob=models.ForeignKey('uploadapp.File', on_delete=models.CASCADE,null=True,blank=True)


class Clases(models.Model):
    nombre=models.CharField(max_length=50,null=False,blank=True)
    tema=models.CharField(max_length=50,null=False,blank=True)
    materias=models.ForeignKey('Cursos.Materias', on_delete=models.CASCADE,null=True,blank=True)
    fecha_inicio=models.DateField(null=False,blank=True)
    profesor=models.ForeignKey('Cursos.Profesores', on_delete=models.CASCADE,null=True,blank=True)


class Subidas(models.Model):
    fecha=models.DateTimeField()
