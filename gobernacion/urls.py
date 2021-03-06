"""gobernacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static

from uploadapp.views import FileView
from uploadapp.views import EntregasView
from uploadapp.views import SubidasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration', include('rest_auth.registration.urls')),
    path('upload/', include('uploadapp.urls')),
    path('entregas/<int:pk>', EntregasView.as_view()),
    path('subidas/<int:pk>', SubidasView.as_view()),
    path('uploads/<int:pk>', FileView.as_view()),
    url('api/gobernacion/users/', include(('Users.urls', 'usuarios'), namespace='usuarios')),
    url('api/gobernacion/cursos/', include(('Cursos.urls', 'cursos'), namespace='cursos')),

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)