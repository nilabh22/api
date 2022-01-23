from django.conf.urls import url
from EventdbApp import views

urlpatterns = [
    url(r'^event$', views.eventApi),
    url(r'^department/([0-9]+)$', views.eventApi)
]
