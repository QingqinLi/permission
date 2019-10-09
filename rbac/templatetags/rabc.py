# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import template
from django.conf import settings
import re

register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_list = request.session.get(settings.MENU_SESSION_KEY)

    for i in menu_list:
        url = i['url']
        if re.match('^{}$'.format(url), request.path_info):
            i['class'] = 'active'
    return {'menu_list': menu_list}