from django.urls import path
from snippets import views1
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views1.snippet_list),
    path('snippets/<int:pk>/', views1.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
