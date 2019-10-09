# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from django.conf import settings
from rbac.server.init_permission import init_permission


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

        init_permission(user, request)

        return redirect(reverse('customer'))

    return render(request, 'login.html')
