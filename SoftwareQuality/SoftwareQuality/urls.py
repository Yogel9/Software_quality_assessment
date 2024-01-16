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
from django.contrib import admin
from django.urls import path, include, re_path

import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halstead/', include('halstead.urls')),
    path('chepin/', include('chepin.urls')),
    path('martin/', include('martin.urls')),
    path('', include('cod_handler.urls'), name='cod_handler'),
    path('', views.main_index, name='main'),
    path('api/pdf', views.get_pdf, name='get_pdf'),


]
