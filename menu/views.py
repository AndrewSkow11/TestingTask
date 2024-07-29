from django.shortcuts import render
from .models import MenuItem

from django.shortcuts import render
from .models import MenuItem

def build_menu_tree(parent=None):
    items = MenuItem.objects.filter(parent=parent)
    tree = []
    for item in items:
        children = build_menu_tree(item)
        tree.append({
            'item': item,
            'children': children,
        })
    return tree

def home(request):
    menu_tree = build_menu_tree()
    return render(request, 'menu/home.html', {'menu_tree': menu_tree})