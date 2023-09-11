"""
URL configuration for hngproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from hngapp2.views import create_person, read_person, update_person, delete_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', create_person, name='create_person'),
    path('api/<int:user_id>/', read_person, name='read_person'),
    path('api/<int:user_id>/update/', update_person, name='update_person'),
    path('api/<int:user_id>/delete/', delete_person, name='delete_person'),
]
