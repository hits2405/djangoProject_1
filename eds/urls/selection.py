from rest_framework import routers
from eds.views.selection import SelectionViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register('', SelectionViewSet)

urlpatterns += router.urls