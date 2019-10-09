from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse
import re


# class PermissionMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         # 对权限进行校验
#         # 1. 当前访问的URL
#         current_url = request.path_info
#
#         # 白名单的判断
#         for i in settings.WHITE_URL_LIST:
#             if re.match(i,current_url):
#                 return
#
#         # 2. 获取当前用户的所有权限信息
#
#         permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
#         # 3. 权限的校验
#         print(current_url)
#
#         for item in permission_list:
#             url = item[0]
#             if re.match("^{}$".format(url), current_url):
#                 return
#         else:
#             return HttpResponse('没有权限')

class PermissionMiddle(MiddlewareMixin):
    def process_request(self, request):
        #  对权限进行校验，1、当前访问的url，白名单的判断 2、获取当前用户的所有权限信息，3、权限的校验
        url = request.path_info
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        for white in settings.WHITE_URL_LIST:
            if re.match(white, url):
                return
        for item in permission_list:

            my_url = item['url']
            print('my_url', my_url)
            if re.match(my_url, url):
                return
        # if [url] in permission_list:
        #     return
        else:
            return HttpResponse('无访问权限')

