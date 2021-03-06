"""web URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from loginfunction import views as login
from loginfunction import urls as login_urls
from loginfunction.views import part_flush
from loginfunction.views import video

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include((login_urls,'login'),namespace='login')),
    url(r'^index/', login.index,name="index"),
    url(r'^charts/', login.charts,name="charts"),
    url(r'^tables/', login.tables,name="tables"),
    url(r'^video/', login.video,name="video"),
    url(r'^part_flush/',part_flush),
]
