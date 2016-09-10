# -*- coding: utf-8 -*
""" tts/model.py

TTS に関する DB 設定を行います。
この データベース では基本的に OpenJTalk を利用するための
Path 関係を管理します。
"""
from __future__ import unicode_literals
from django.db import models


class OpenJTalk(models.Model):
    """
    Open JTalk への Path を管理します
    """
    openJTalk = models.FilePathField()


class Roid(models.Model):
    """
    各キャラクターの音響モデル及び、表示用画像へのパスを管理します。
    """
    name = models.CharField(max_length=256)
    voiceModel = models.FileField(upload_to='voices/%Y/%m/%d/')
    figure = models.ImageField(upload_to='figure/%Y/%m/%d/')
