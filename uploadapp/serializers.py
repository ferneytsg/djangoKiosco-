from rest_framework import serializers

from .models import File
from Cursos.serializers import EntregasSerializers
from Cursos.models import Entregas


class FileSerializer(serializers.ModelSerializer):
    entrega_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Entregas.objects.all(),
                                                       source='entrega')

    class Meta:
        model = File
        fields = "__all__"