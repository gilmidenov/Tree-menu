from django.shortcuts import render
from app.templatetags.menu_tags import get_menu_items


def menu_view(request):
    menu_items = get_menu_items()
    return render(request, 'menu.html', {'items': menu_items})
