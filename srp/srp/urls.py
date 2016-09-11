# -*- coding: utf-8 -*
""" srp/urls.py

WEB アプリとしての srp 全体の URL を管理します。
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^web/', include('index.urls')),
    url(r'^web/admin/', admin.site.urls),
    url(r'^web/roid', include('tts.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
