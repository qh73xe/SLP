# -*- coding: utf-8 -*
""" tts.admin.py

tts のモデルの値を WEB UI 上で管理します。
なおこの機能は admin のみが使用可能です。
"""
from django.contrib import admin
from .models import OpenJTalk, Roid

admin.site.register(OpenJTalk)
admin.site.register(Roid)
