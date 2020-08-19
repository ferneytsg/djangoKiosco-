from django.db import models



class File(models.Model):
    codigo = models.IntegerField(unique=True,primary_key=True)
    file = models.FileField(blank=False, null=False)
    subida = models.ForeignKey('Cursos.Subidas', on_delete=models.CASCADE, null=True, blank=True)
    entrega = models.ForeignKey('Cursos.Entregas', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.file.name



