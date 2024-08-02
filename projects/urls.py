from rest_framework import routers
from .api import ProjectViewSet

# Esto genera las 4 rutas básicas para un API
router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls