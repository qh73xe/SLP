# -*- coding: utf-8 -*
""" index/urls.py

SRP のインデックスページ URL を管理します。
"""
from django.conf.urls import url
from .views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index')
]
