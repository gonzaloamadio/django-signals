from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
app_name='entities'
router = DefaultRouter()
router.register(r'persons2', views.Person2ViewSet, base_name="entities2-persons")
router.register(r'companies2', views.Company2ViewSet, base_name="entities2-companies")
urlpatterns = router.urls

