from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'bgapp'

urlpatterns=[
     path('' , views.post_list, name='postlist'),
     path('create/', views.post_create,name='postcreate'),
     path('detail/', views.post_detail,name='postdetail'),
     path('update/', views.post_update,name='postupdate'),
     path('delete/', views.post_delete,name='postdelete'),
 ]



#
# urlpatterns = [
#     url(r'^$',"views.post_list"),
#     url(r'^create/$',"views.post_create"),
#     url(r'^detail/$',"views.post_detail"),
#     url(r'^update/$',"views.post_update"),
#     url(r'^delete/$',"views.post_delete"),
# ]

"""path('', views.post_create,name='postcreate'),
    path('', views.post_detail,name='postdetail'),

    path('', views.post_update,name='postupdate'),
    path('', views.post_delete,name='postdelete'),
"""
'''
urlpatterns = [
    path('',views.create_profile,name='create'),

]
'''
#this are URL to navigate



