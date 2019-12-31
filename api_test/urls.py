# encoding=utf-8
"""
@AUthor:Reese
@Date:2019/12/29 22:41
@Description:
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'add_book$', add_book, ),
    url(r'show_books$', show_books, ),
]