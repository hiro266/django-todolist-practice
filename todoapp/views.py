from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import TodoModel

# ListView = Readに適したview
class TodoList(ListView):
    template_name = 'list.html'
    # 使用するモデルを指定
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # formでTodoモデルのどのカラムを使用するか指定する
    # モデルにないカラムを指定するとエラー出力
    fields = ('title', 'memo', 'priority', 'duedate')
    # データの作成が完了した時のリダイレクト先
    # urlsで指定したnameを入力
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')