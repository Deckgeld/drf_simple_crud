from rest_framework import serializers
from .models import Project

# Esta clase se encarga de serializar los datos de los proyectos
# serializar es convertir los datos en un formato que se pueda enviar por la red
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)