# 管理画面の操作をするために使う
from django.contrib import admin
from .models import TodoModel

admin.site.register(TodoModel)