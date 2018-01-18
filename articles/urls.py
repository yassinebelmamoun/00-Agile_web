from django.conf.urls import include, url
from . import views

urlpatterns = [
    path(r'', views.first_view, name="v")
]
~   
