"""SoftwareQuality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("halstead/", include("app.halstead.urls")),
    path("chepin/", include("app.chepin.urls")),
    path("martin/", include("app.martin.urls")),
    path("", include("app.cod_handler.urls"), name="cod_handler"),
    path("", views.main_index, name="main"),
    path("api/pdf", views.get_pdf, name="get_pdf"),
]
