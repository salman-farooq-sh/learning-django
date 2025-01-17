from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views5

router = DefaultRouter()
router.register(r"snippets", views5.SnippetViewSet, basename="snippet")
router.register(r"users", views5.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
