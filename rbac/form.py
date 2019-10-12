# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import forms
from rbac import models
from django.utils.safestring import mark_safe


class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ['name']

        widgets = {
            'name': forms.widgets.Input(attrs={'class': 'form-control'})
        }


ICON_LIST = [['fa-address-book', '<i aria-hidden="true" class="fa fa-address-book"></i>'],
             ['fa-address-book', '<i aria-hidden="true" class="fa fa-address-book"></i>'],
             ['fa-address-book-o', '<i aria-hidden="true" class="fa fa-address-book-o"></i>'],
             ['fa-address-card', '<i aria-hidden="true" class="fa fa-address-card"></i>'],
             ['fa-address-card-o', '<i aria-hidden="true" class="fa fa-address-card-o"></i>'],
             ['fa-adjust', '<i aria-hidden="true" class="fa fa-adjust"></i>'],
             ['fa-american-sign-language-interpreting',
              '<i aria-hidden="true" class="fa fa-american-sign-language-interpreting"></i>'],
             ['fa-anchor', '<i aria-hidden="true" class="fa fa-anchor"></i>'],
             ['fa-archive', '<i aria-hidden="true" class="fa fa-archive"></i>'],
             ['fa-area-chart', '<i aria-hidden="true" class="fa fa-area-chart"></i>'],
             ['fa-arrows', '<i aria-hidden="true" class="fa fa-arrows"></i>'],
             ['fa-arrows-h', '<i aria-hidden="true" class="fa fa-arrows-h"></i>'],
             ['fa-arrows-v', '<i aria-hidden="true" class="fa fa-arrows-v"></i>'],
             ['fa-asl-interpreting', '<i aria-hidden="true" class="fa fa-asl-interpreting"></i>'],
             ['fa-assistive-listening-systems', '<i aria-hidden="true" class="fa fa-assistive-listening-systems"></i>'],
             ['fa-asterisk', '<i aria-hidden="true" class="fa fa-asterisk"></i>'],
             ['fa-at', '<i aria-hidden="true" class="fa fa-at"></i>'],
             ['fa-audio-description', '<i aria-hidden="true" class="fa fa-audio-description"></i>'],
             ['fa-automobile', '<i aria-hidden="true" class="fa fa-automobile"></i>'],
             ['fa-balance-scale', '<i aria-hidden="true" class="fa fa-balance-scale"></i>'],
             ['fa-ban', '<i aria-hidden="true" class="fa fa-ban"></i>'],
             ['fa-bank', '<i aria-hidden="true" class="fa fa-bank"></i>'],
             ['fa-bar-chart', '<i aria-hidden="true" class="fa fa-bar-chart"></i>'],
             ['fa-bar-chart-o', '<i aria-hidden="true" class="fa fa-bar-chart-o"></i>'],
             ['fa-barcode', '<i aria-hidden="true" class="fa fa-barcode"></i>'],
             ['fa-bars', '<i aria-hidden="true" class="fa fa-bars"></i>'],
             ['fa-bath', '<i aria-hidden="true" class="fa fa-bath"></i>'],
             ['fa-bathtub', '<i aria-hidden="true" class="fa fa-bathtub"></i>'],
             ['fa-battery', '<i aria-hidden="true" class="fa fa-battery"></i>'],
             ['fa-battery-0', '<i aria-hidden="true" class="fa fa-battery-0"></i>'],
             ['fa-battery-1', '<i aria-hidden="true" class="fa fa-battery-1"></i>'],
             ['fa-battery-2', '<i aria-hidden="true" class="fa fa-battery-2"></i>'],
             ['fa-battery-3', '<i aria-hidden="true" class="fa fa-battery-3"></i>'],
             ['fa-battery-4', '<i aria-hidden="true" class="fa fa-battery-4"></i>'],
             ['fa-battery-empty', '<i aria-hidden="true" class="fa fa-battery-empty"></i>'],
             ['fa-battery-full', '<i aria-hidden="true" class="fa fa-battery-full"></i>'],
             ['fa-battery-half', '<i aria-hidden="true" class="fa fa-battery-half"></i>'],
             ['fa-battery-quarter', '<i aria-hidden="true" class="fa fa-battery-quarter"></i>'],
             ['fa-battery-three-quarters', '<i aria-hidden="true" class="fa fa-battery-three-quarters"></i>'],
             ['fa-bed', '<i aria-hidden="true" class="fa fa-bed"></i>'],
             ['fa-beer', '<i aria-hidden="true" class="fa fa-beer"></i>'],
             ['fa-bell', '<i aria-hidden="true" class="fa fa-bell"></i>'],
             ['fa-bell-o', '<i aria-hidden="true" class="fa fa-bell-o"></i>'],
             ['fa-bell-slash', '<i aria-hidden="true" class="fa fa-bell-slash"></i>'],
             ['fa-bell-slash-o', '<i aria-hidden="true" class="fa fa-bell-slash-o"></i>'],
             ['fa-bicycle', '<i aria-hidden="true" class="fa fa-bicycle"></i>'],
             ['fa-binoculars', '<i aria-hidden="true" class="fa fa-binoculars"></i>'],
             ['fa-birthday-cake', '<i aria-hidden="true" class="fa fa-birthday-cake"></i>'],
             ['fa-blind', '<i aria-hidden="true" class="fa fa-blind"></i>'],
             ['fa-bluetooth', '<i aria-hidden="true" class="fa fa-bluetooth"></i>'],
             ['fa-bluetooth-b', '<i aria-hidden="true" class="fa fa-bluetooth-b"></i>'],
             ['fa-bolt', '<i aria-hidden="true" class="fa fa-bolt"></i>'],
             ['fa-bomb', '<i aria-hidden="true" class="fa fa-bomb"></i>'],
             ['fa-book', '<i aria-hidden="true" class="fa fa-book"></i>'],
             ['fa-bookmark', '<i aria-hidden="true" class="fa fa-bookmark"></i>'],
             ['fa-bookmark-o', '<i aria-hidden="true" class="fa fa-bookmark-o"></i>'],
             ['fa-braille', '<i aria-hidden="true" class="fa fa-braille"></i>'],
             ['fa-briefcase', '<i aria-hidden="true" class="fa fa-briefcase"></i>'],
             ['fa-bug', '<i aria-hidden="true" class="fa fa-bug"></i>'],
             ['fa-building', '<i aria-hidden="true" class="fa fa-building"></i>']]


class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['title',
                  'weight',
                  'icon']

        widgets = {
            'title': forms.widgets.Input(attrs={'class': 'form-control'}),
            'weight': forms.widgets.Input(attrs={'class': 'form-control'}),
            'icon': forms.widgets.RadioSelect(choices=[[i[0], mark_safe(i[1])] for i in ICON_LIST]),
        }


class PermissionForm(forms.ModelForm):
    class Meta:
        model = models.Permission

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})