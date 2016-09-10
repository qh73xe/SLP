# -*- coding: utf-8 -*
""" srp/urls.py

WEB アプリとしての srp 全体の URL を管理します。
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^web/', include('index.urls')),
    url(r'^admin/', admin.site.urls),
]
