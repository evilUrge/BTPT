"""btpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from games.views import *
from users.views import *

router = routers.DefaultRouter()

# Users
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Games
router.register(r'games', GamesViewSet)
router.register(r'quests', QuestsViewSet)  # Todo: Make this as part of the same game id!
router.register(r'publisher', PublishersViewSet)
router.register(r'developers', DevelopersViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls'))
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
