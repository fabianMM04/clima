from django.conf.urls import url
from . import views
from .views import LiCoor, RegCoor
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lis/coor/$', LiCoor.as_view(), name='lis_coor'),
    url(r'^reg/coor/$', RegCoor.as_view(), name='reg_coor'),
]

