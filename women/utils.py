from copy import deepcopy
from django.db.models import Count

from .models import *
menu = [{'title': "О сайте", 'url_name': 'women:about'},
        {'title': "Добавить статью", 'url_name': 'women:add_page'},
        {'title': "Обратная связь", 'url_name': 'women:contact'},
]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, context, **kwargs):
        context.update(kwargs)
        cats = Category.objects.all()
        # copy не копирует вложенные файлы, а оставляет их ссылками, они в последствии могут быть изменнеы случайно
        user_menu = deepcopy(menu)
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
