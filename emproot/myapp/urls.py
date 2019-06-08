from rest_framework.routers import SimpleRouter
from .views import EmployeeViewSet


router = SimpleRouter()
router.register(r'employees', EmployeeViewSet)
urlpatterns = router.urls