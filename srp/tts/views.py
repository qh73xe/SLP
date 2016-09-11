# -*- coding: utf-8 -*
""" tts.views.py

OpenJtalk 用の Views
"""
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Roid
from .forms import TalkForm

class RoidCreate(CreateView):
    model = Roid
    page_name = 'roid_create'
    fields = ['name', 'voiceModel', 'figure']
    success_url = reverse_lazy('roid_list')

    def get_context_data(self, **kwargs):
        context = super(RoidCreate, self).get_context_data(**kwargs)
        headline = {
            'title': ' ROID を登録',
            'bodies': [
                '好きな ROID を登録することができます。',
                'これには、その ROID の音響モデルを作成する必要があります',
            ]
        }
        context['headline'] = headline
        return context

class RoidUpdate(UpdateView):
    model = Roid
    page_name = 'roid_update'
    fields = ['name', 'voiceModel', 'figure']

    def get_context_data(self, **kwargs):
        context = super(RoidUpdate, self).get_context_data(**kwargs)
        headline = {
            'title': ' ROID 情報を更新',
            'bodies': [
                '好きな ROID を登録することができます。',
                'これには、その ROID の音響モデルを作成する必要があります',
            ]
        }
        context['headline'] = headline
        return context


class RoidList(ListView):
    model = Roid
    page_name = 'roid_list'

    def get_context_data(self, **kwargs):
        context = super(RoidList, self).get_context_data(**kwargs)
        headline = {
            'title': ' ROID 一覧',
            'bodies': [
                'SRP に登録されている ROID 一覧です',
            ]
        }
        context['headline'] = headline
        return context


class RoidDetail(FormView, DetailView):
    model = Roid
    page_name = 'roid_detail'
    success_url = page_name
    form_class = TalkForm
    template_name = 'tts/roid_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RoidDetail, self).get_context_data(**kwargs)
        headline = {
            'title': 'RIOD 詳細',
            'bodies': [
                'ここから ROID に話をさせることができます。',
            ]
        }
        context['form'] = self.get_form()
        context['headline'] = headline
        return context

    def post(self, request, *args, **kwargs):
        from django.shortcuts import render
        form = self.form_class(request.POST)
        if form.is_valid():
            args =  form.get_cleaned_datas()
            self.object = self.get_object()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            self.object.talk(*args)
            context['args'] = args
            context['wav'] = self.object.jt.wav_url
            return render(request, self.template_name, context)
