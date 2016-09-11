# -*- coding: utf-8 -*
""" tts/model.py

TTS に関する DB 設定を行います。
この データベース では基本的に OpenJTalk を利用するための
Path 関係を管理します。
"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from srp.settings import BIN_DIR

@python_2_unicode_compatible
class OpenJTalk(models.Model):
    """
    Open JTalk への Path を管理します
    """
    openJTalk = models.FilePathField('path', path=BIN_DIR)

    def __str__(self):
        return self.openJTalk


class Roid(models.Model):
    """
    各キャラクターの音響モデル及び、表示用画像へのパスを管理します。
    """
    name = models.CharField(
        '名前',
        max_length=256
    )
    voiceModel = models.FileField(
        '音響モデル',
        upload_to='voices/%Y/%m/%d/'
    )
    figure = models.ImageField(
        '画像',
        upload_to='figure/%Y/%m/%d/'
    )

    def talk(
            self, text, log=False,
             speech_speed=None, half_tone=None,
            log_F0=None, spectrum=None, all_pass=None
        ):
        from .talk import OpenJTalk
        jt = OpenJTalk()
        jt.set_voiceModel(self.voiceModel.path)
        jt.run(text, log, speech_speed, half_tone, log_F0, spectrum, all_pass)
        self.jt = jt
