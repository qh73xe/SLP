# -*- coding: utf-8 -*
""" index/views.py

SRP のインデックスに関する View を管理します。
"""
from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    """
    初期画面作成用クラス
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        headline = {
            'title': 'Speech Roid Project',
            'bodies': [
                ''
            ]
        }
        context['headline'] = headline
        return context
