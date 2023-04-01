from django import template
from app.models import MenuItem

register = template.Library()


def get_menu_items(parent=None):
    if parent is None:
        menu_items = MenuItem.objects.filter(parent__isnull=True)
    else:
        menu_items = MenuItem.objects.filter(parent=parent)
    return menu_items


@register.inclusion_tag('menu.html')
def show_menu_items(parent=None):
    menu_items = get_menu_items(parent)
    return {'items': menu_items}
