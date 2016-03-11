from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
     url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
     url(r'^vote/(?P<pk>\d+)/$', views.vote, name='vote'),
     url(r'^sign/page/$', views.sign_page, name='sign_page'),
     url(r'^register/user/$',views.register_user,name='register_user'),
     url(r'^register/success/$',views.register_success,name='register_success'),

]