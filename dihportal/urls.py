"""dihportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from registrations import views as reg_views
from projects import views as pro_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', reg_views.index, name='index'),
    url(r'^tokensignin$', reg_views.callback, name='callback'),
    url(r'^dashboard$', reg_views.dashboard, name='dashboard'),
    url(r'^proposal$', reg_views.proposal, name='proposal'),
    url(r'^profile$', reg_views.profile, name='profile'),
    url(r'^user$', reg_views.user, name='user'),
    url(r'^fill$', pro_views.fill, name='fill'),
    url(r'^secondfill$', pro_views.secondfill, name='secondfill'),
    url(r'^evaluation$', pro_views.evaluation, name='evaluation'),
    url(r'^projects', pro_views.projects, name='projects'),
]
