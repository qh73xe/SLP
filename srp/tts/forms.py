# -*- coding: utf-8 -*
""" tts/forms.py

tts 用のフォームを管理します。
"""
from django import forms
from django.forms import NumberInput

class TalkForm(forms.Form):
    text = forms.CharField(label='何を言う？', max_length=200)
    speech_speed = forms.FloatField(
        label='発話速度',
        required=False,
        widget=NumberInput(
            attrs={'type':'range', 'value': '0', 'min': '-2', 'max': '2', 'step': '0.1' }
        )
    )
    half_tone = forms.FloatField(
        label='高さ',
        required=False,
        widget=NumberInput(
            attrs={'type':'range', 'value': '0', 'min': '-2', 'max': '2', 'step': '0.1' }
        )
    )
    log_F0 = forms.FloatField(
        label='抑揚',
        required=False,
        widget=NumberInput(
            attrs={'type':'range', 'value': '0', 'min': '-2', 'max': '2', 'step': '0.1' }
        )
    )
    spectrum = forms.FloatField(
        label='かすれ具合',
        required=False,
        widget=NumberInput(
            attrs={'type':'range', 'value': '0', 'min': '-1', 'max': '1', 'step': '0.1' }
        )
    )
    all_pass = forms.FloatField(
        label='位相変換',
        required=False,
        widget=NumberInput(
            attrs={'type':'range', 'value': '0', 'min': '-1', 'max': '1', 'step': '0.1' }
        )
    )
    def get_cleaned_datas(self):
        """
        バリデーションが通った後に OpenJtalk 用の引き数に加工します。

        text (str): 発話する文字列
        log (bool): ログファイルを残す [False]
        speech_speed (float): 発話速度 [1.0][0.0--*]
        half_tone(float): 声の高さ [0.0][*--*]
        all_pass (float): 位相変換 [0.0--1.0]
        log_F0 (float): 抑揚 [1.0][0.0--*]
        """
        text = self.cleaned_data['text']
        if isinstance(text, str):
            text = unicode(text)

        log = True

        speech_speed = self.cleaned_data['speech_speed']
        if speech_speed:
            speech_speed = speech_speed + 2.0
        else:
            speech_speed = None

        half_tone = self.cleaned_data['half_tone']
        if not half_tone:
            half_tone = None
        else:
            half_tone = half_tone * 10.0

        log_F0 = self.cleaned_data['log_F0']
        if log_F0:
            log_F0 = (log_F0 + 2.0) * 10.0
        else:
            log_F0 = None

        spectrum = self.cleaned_data['spectrum']
        if spectrum:
            spectrum = (spectrum + 1.0) * 0.1
        else:
            spectrum = None

        all_pass = self.cleaned_data['all_pass']
        if all_pass:
            all_pass = (all_pass + 1.0) * 0.1
        else:
            all_pass = None

        return text, log, speech_speed, half_tone, log_F0, spectrum, all_pass
