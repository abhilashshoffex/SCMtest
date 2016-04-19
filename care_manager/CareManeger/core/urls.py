from django.conf.urls import include, url
from .views import index, submited

urlpatterns = [
	url(r'^$', index, name="index"),
	url(r'^submited/$', submited, name="submited"),
]