from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from record.views import ClientsAPIView, ClientsCreateAPIView

urlpatterns = [
    path('list/', ClientsAPIView.as_view()),
    path('create/', ClientsCreateAPIView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]