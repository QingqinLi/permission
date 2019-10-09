# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from django.conf import settings


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pwd')
        user = models.User.objects.filter(name=user, password=password).first()
        if not user:
            err_msg = '用户名或者密码错误'
            return render(request, 'login.html', {'err_msg': err_msg})
        # 登录成功
        # 将权限信息写入到session中

        # 查询当前登录用户有的权限, 跨表查询
        permission_list = user.roles.all().filter(permissions__url__isnull=False).values_list('permissions__url').distinct()
        # 过滤空权限，重复权限
        # 将权限信息写入session,会自动进行序列化, permission_list应该是可配置的，setting
        request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)



        return redirect(reverse('customer'))

    return render(request, 'login.html')