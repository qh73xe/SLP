# -*- coding: utf-8 -*
""" tts.urls.py

TTS モジュールの URL を管理します。
"""
from django.conf.urls import url

from .views import (
    RoidCreate,
    RoidUpdate,
    RoidList,
    RoidDetail,
)

urlpatterns = [
    url(r'^create$', RoidCreate.as_view(), name=RoidCreate.page_name),
    url(r'^list$', RoidList.as_view(), name=RoidList.page_name),
    url(r'^update/(?P<pk>\d+)/$', RoidUpdate.as_view(), name=RoidUpdate.page_name),
    url(r'^detail/(?P<pk>\d+)/$', RoidDetail.as_view(), name=RoidDetail.page_name),
]
