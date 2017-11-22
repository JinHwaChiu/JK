"""MySite URL Configuration

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

from Mylearn import views as Mylearn_views #new item
from calculate import views as calculate_views #new item


urlpatterns = [

    url(r'^$', Mylearn_views.index),  # new
    url(r'^add/$', calculate_views.add),  # new
    url(r'^admin/', admin.site.urls),
    url(r'^add/(\d+)/(\d+)/$', calculate_views.add2, name = 'add2'),
    url(r'^home/$',calculate_views.home,name = 'home'),
    url(r'tutorial/$',calculate_views.tutorial,name = 'tutor'),
    url(r'infodic/$',calculate_views.info_dic,name ='info'),
    url(r'map/$',calculate_views.Map, name='map'),
    url(r'bootstrap/$',calculate_views.bootstrap, name='boot'),
]
