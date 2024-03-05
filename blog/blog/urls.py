"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from categories.api.router import router_categories
from posts.api.router import router_post
from comments.api.router import router_comments


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API", # give it a title
      default_version='v1', # give it a version
      description="Documentacion de la API del Blog UDEMY", #description
      terms_of_service="", #give url to terms & conditions if you have one 
      contact=openapi.Contact(email="superadmin@gmail.com"), #give email
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include ('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_post.urls)),
    path('api/', include (router_comments.urls),)
]

