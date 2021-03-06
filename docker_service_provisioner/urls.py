from django.conf.urls import patterns, include, url
from docker_service_provisioner.views import ServiceInstanceProvisionAPIView, ServiceInstanceUpdateDeleteAPIView

urlpatterns = patterns('',
    url(r'^dockerfile/(?P<service>\w+)/(?P<version>\d{1,4})/$', 'docker_service_provisioner.views.dockerfile', name='dockerfile'),
    url(r'^(?P<service>\w+)/resources$', ServiceInstanceProvisionAPIView.as_view(), name='heroku_api_provision'),
    url(r'^(?P<service>\w+)/resources/(?P<uuid>\w+)$', ServiceInstanceUpdateDeleteAPIView.as_view(), name='heroku_api_delete'),
)
