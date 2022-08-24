from django.contrib import admin
from django.urls import path

from .views import *
from django.conf.urls import url

urlpatterns = [
#     path('admin/', admin.site.urls),
    url(r'^v1/agora-token/$', AgoraToken.as_view(), name='agora-token'), # for agora api 

    
]