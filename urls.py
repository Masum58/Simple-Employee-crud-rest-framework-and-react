from django.db import router
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router= DefaultRouter()
router.register(r'employee',EmployeeViewSet,basename='employe')

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
