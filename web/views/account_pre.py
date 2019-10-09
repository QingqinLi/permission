from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from django.conf import settings

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        
        user = models.User.objects.filter(name=username, password=pwd).first()
        
        if not user:
            err_msg = '用户名或密码错误'
            return render(request, 'login.html', {'err_msg': err_msg})
        
        # 登录成功
        # 将权限信息写入到session
        
        # 1. 查当前登录用户拥有的权限
        permission_list = user.roles.filter(permissions__url__isnull=False).values_list(
                                                                                   'permissions__url').distinct()
        # for i in permission_list:
        #     print(i)
        
        # 2. 将权限信息写入到session
        print("permission_list",permission_list)
        print("permission_list_1",list(permission_list))
        request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)
        
        
        return redirect(reverse('customer'))
    
    return render(request, 'login.html')
