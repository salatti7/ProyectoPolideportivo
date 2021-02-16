from django.urls import include, path
from rest_framework import routers
from prueba import views
from polideportivo.views import PistaViewSet, ReservaViewSet, HorarioViewSet, TarifaViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'pista', PistaViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'reserva', ReservaViewSet)
router.register(r'tarifa', TarifaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) ]