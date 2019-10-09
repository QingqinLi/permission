# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf import settings


# 解耦
def init_permission(user, request):
    # 查询当前登录用户有的权限, 跨表查询
    permission_query = user.roles.all().filter(permissions__url__isnull=False).values('permissions__url',
                                                                                      'permissions__is_menu',
                                                                                      'permissions__icon',
                                                                                      'permissions__title'
                                                                                      ).distinct()
    permission_list = []
    # 存在菜单信息
    menu_list = []
    for i in permission_query:
        permission_list.append({'url': i['permissions__url']})
        if i['permissions__is_menu']:
            # 用字典，查询速度快
            menu_list.append({'url': i['permissions__url'], 'icon': i['permissions__icon'],
                              'title': i['permissions__title']})
    print(permission_list)

    # 过滤空权限，重复权限
    # 将权限信息写入session,会自动进行序列化, permission_list应该是可配置的，setting
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list