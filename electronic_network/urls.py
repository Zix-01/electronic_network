from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, RetailNetworkViewSet, EntrepreneurViewSet

router = DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'retail-networks', RetailNetworkViewSet)
router.register(r'entrepreneurs', EntrepreneurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
