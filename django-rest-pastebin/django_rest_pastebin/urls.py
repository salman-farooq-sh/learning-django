from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include('snippets.urls6')),
    # path("", include("snippets.urls5")),
    # path('', include('snippets.urls4')),
    # path('', include('snippets.urls3')),
    # path('', include('snippets.urls2')),
    # path('', include('snippets.urls1')),
]
