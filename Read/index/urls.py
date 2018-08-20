from django.conf.urls import url,include
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^login/',login_views,name='login'),
    url(r'^registe',registe_views,name='registe'),
    url(r'^login1',login1_views,name='login1'),
    url(r'^index',index_views,name='index'),
    url(r'^look',look_views,name='look'),
    url(r'^detail/(\d{2})',detail_views,name='detail'),
    url(r'^commit/',commit_views,name='commit'),
    url(r'^login_out/',loginout_views,name='loginout'),
    url(r'^get_commit/',get_views,name='get'),
    url(r'^code/',check_code),
    url(r'^very/',verifyTest),
    url(r'^login_ajax',ajax_views),
]


