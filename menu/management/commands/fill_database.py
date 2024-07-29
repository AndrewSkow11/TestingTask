from django.core.management.base import BaseCommand
from menu.models import MenuItem

class Command(BaseCommand):
    help = 'Fill the database with test data'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        MenuItem.objects.all().delete()

        # Создаем тестовые данные
        menu_items = [
            {'title': 'Home', 'url': 'http://example.com/home'},
            {'title': 'About', 'url': 'http://example.com/about'},
            {'title': 'Contact', 'url': 'http://example.com/contact'},
            {'title': 'Services', 'url': 'http://example.com/services'},
            {'title': 'Blog', 'url': 'http://example.com/blog'},
        ]

        for item in menu_items:
            MenuItem.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Database has been filled with test data!'))