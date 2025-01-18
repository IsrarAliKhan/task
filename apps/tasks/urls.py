from rest_framework.routers import DefaultRouter

from apps.tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks',TaskViewSet, basename='tasks')

urlpatterns = router.urls
