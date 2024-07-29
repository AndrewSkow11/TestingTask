from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    # Получаем все пункты меню с заданным именем
    menu_items = MenuItem.objects.filter(parent__isnull=True)

    def get_children(item):
        return item.children.all()

    def is_active(item):
        return current_url == item.url or (item.named_url and request.resolver_match.url_name == item.named_url)

    def build_menu(items):
        menu_html = '<ul>'
        for item in items:
            active_class = 'active' if is_active(item) else ''
            menu_html += f'<li class="{active_class}">{item.title}'
            children = get_children(item)
            if children.exists():
                menu_html += build_menu(children)
            menu_html += '</li>'
        menu_html += '</ul>'
        return menu_html

    return build_menu(menu_items)
