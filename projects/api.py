from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

#  Los viewsets son una forma de agrupar las vistas de Django
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer