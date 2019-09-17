
from django.contrib import admin
from django.urls import path
from announce import views
from account import views as ac_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', ac_views.signup,name='signup'),
    path('',views.index,name='index'),
    path('register/',ac_views.register,name='register'),
    path('select/',ac_views.select,name='select'),
    url(r'^colleges/(?P<pk>\d+)/$',ac_views.col_schools,name='col_schools'),
    url(r'^colleges/(?P<pk>\d+)/new$',ac_views.nu_school,name='nu_school'),
    url(r'^colleges/(?P<pk>\d+)/schools/(?P<skl_pk>\d+)/$', ac_views.skl_departs, name='skl_deprts'),
    url(r'^colleges/(?P<pk>\d+)/schools/(?P<skl_pk>\d+)/new$', ac_views.nu_depart, name='nu_depart'),
    url(r'^colleges/(?P<pk>\d+)/schools/(?P<skl_pk>\d+)/departments/(?P<depart_pk>\d+)/$', ac_views.depart_levels, name='depart_levels'),
    url(r'^colleges/(?P<pk>\d+)/schools/(?P<skl_pk>\d+)/departments/(?P<depart_pk>\d+)/new$', ac_views.nu_level, name='nu_level')
]
