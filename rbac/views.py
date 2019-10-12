from django.shortcuts import render, redirect, reverse
from rbac import models
from rbac import form
from django.db.models import Q


# Create your views here.
def role_list(request):
    all_roles = models.Role.objects.all()

    return render(request, 'rbac/role_list.html', {'all_roles': all_roles})


def role(request, role_id=None):
    my_role = models.Role.objects.filter(id=role_id).first()
    role_obj = form.RoleForm(instance=my_role)

    if request.method == 'POST':
        role_obj = form.RoleForm(request.POST, instance=my_role)
        if role_obj.is_valid():
            role_obj.save()
            return redirect(reverse('rbac:role_list'))
    return render(request, 'rbac/role_add.html', {'role_obj': role_obj})


def role_del(request, role_id):
    models.Role.objects.filter(id=role_id).delete()
    return redirect(reverse('rbac:role_list'))


def menu_list(request):
    all_menus = models.Menu.objects.all()
    mid = request.GET.get("mid")
    permission_dict = {}
    if mid:
        permissions_query = models.Permission.objects.filter(Q(menu_id=mid) | Q(parent__menu_id=mid))
    else:
        permissions_query = models.Permission.objects.all()
    all_permissions = permissions_query.values()
    for permission in all_permissions:
        if permission.get('menu_id'):
            permission_dict[permission['id']] = permission
            permission_dict[permission['id']]['child'] = []
    for permission in all_permissions:
        pid = permission['parent_id']
        if pid:
            permission_dict[pid]['child'].append(permission)
    print("permission_dict", permission_dict)

    return render(request, 'rbac/menu_list.html', {'all_menus': all_menus,
                                                   'all_permissions': permission_dict,
                                                   })


def menu(request, edit_id=None):
    menu_obj = models.Menu.objects.filter(id=edit_id).first()
    form_obj = form.MenuForm(instance=menu_obj)
    if request.method == 'POST':
        form_obj = form.MenuForm(request.POST, instance=menu_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))

    return render(request, 'rbac/menu_add.html', {'form_obj': form_obj})


def menu_del(request, del_id):
    models.Menu.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:menu_list'))


def permission(request, edit_id=None):
    per_obj = models.Permission.objects.filter(id=edit_id).first()
    form_obj = form.PermissionForm(instance=per_obj)

    if request.method == 'POST':
        form_obj = form.PermissionForm(request.POST, instance=per_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))
    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def permission_del(request, del_id):
    models.Permission.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:menu_list'))

