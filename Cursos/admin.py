from django.contrib import admin

# Register your models here.
from .models import Versiones
from .models import Profesores
from .models import Entregas
from .models import Estudiantes
from .models import Materias
from .models import MaterialEstudio
from .models import Dispositivos
from .models import Subidas
from .models import Evaluaciones
from .models import Grados
from .models import Ejercicios
from .models import Clases
from .models import Planeacion
from .models import Tareas
from .models import UserLMS


admin.site.register(Versiones)
admin.site.register(Dispositivos)
admin.site.register(Grados)
admin.site.register(Ejercicios)
admin.site.register(Profesores)
admin.site.register(Clases)
admin.site.register(Entregas)
admin.site.register(Estudiantes)
admin.site.register(Evaluaciones)
admin.site.register(MaterialEstudio)
admin.site.register(Materias)
admin.site.register(Planeacion)
admin.site.register(Subidas)
admin.site.register(Tareas)
admin.site.register(UserLMS)





