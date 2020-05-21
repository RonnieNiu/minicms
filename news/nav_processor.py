#-*- coding: utf-8 -*-

'''此函数作用,导航栏的上下文渲染'''

from news.models import Column

def nav_column(request):
    nav_display = Column.objects.filter(nav_display=True)
    return {'nav_display':nav_display}
