from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns=[
path('',views.noor,name='home' ),
path('sum',views.sum,name='summetion')
]