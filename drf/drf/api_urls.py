from rest_framework import routers
from home.api_views import PersonViewset

router = routers.DefaultRouter()
router.register('person', PersonViewset, basename='person')
