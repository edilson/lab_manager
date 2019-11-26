from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_nested import routers
from . import views as views

router = routers.SimpleRouter()
router.register('laboratories', views.LaboratoryViewSet, basename='laboratories')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url('admin/', admin.site.urls),
]
