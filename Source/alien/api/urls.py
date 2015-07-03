from django.conf.urls import url, include
from rest_framework import routers
import views

urlpatterns = [
    url(r'^$', views.APIRoot.as_view(), name='api_root'),
    url(r'^threat/details/$', views.IPDetailsView.as_view(), name='threat_details'),
]