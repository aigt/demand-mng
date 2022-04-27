from rest_framework import routers
from .api import DemandViewSet


router = routers.DefaultRouter()
router.register('api/demand', DemandViewSet, 'demand')


urlpatterns = router.urls