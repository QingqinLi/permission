# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import template
from django.conf import settings
import re
from collections import OrderedDict

register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_order = OrderedDict()
    menu_list = request.session.get(settings.MENU_SESSION_KEY)

    for key in sorted(menu_list, key=lambda x: menu_list[x]['weight'], reverse=True):
        print(key)
        menu_order[key] = menu_list[key]
        menu_order[key]['class'] = 'hide'

        for i in menu_order[key]['children']:
            if i['id'] == request.current_menu_id:
                menu_order[key]['class'] = ''
            if re.match('^{}$'.format(i['url']), request.path_info):
                i['class'] = 'active'
                print("request.current_menu_id", request.current_menu_id)
                # if i['id'] == request.current_menu_id:
                #     menu_order[key]['class'] = ''

    # for menu in menu_list.values():
    #     for i in menu['children']:
    #         if re.match('^{}$'.format(i['url']), request.path_info):
    #             i['class'] = 'active'

    # for i in menu_list:
    #     url = i['url']
    #     if re.match('^{}$'.format(url), request.path_info):
    #         i['class'] = 'active'
    return {'menu_list': menu_order}