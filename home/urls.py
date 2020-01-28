from django.conf.urls import url, include
from .views import index, contact, explained

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^explained/$', explained, name='explained'),
]