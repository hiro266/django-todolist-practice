from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    # name = railsのxxx_pathを自分で作るようなイメージ
    path('list/', TodoList.as_view(), name='list'),
    # pk = primary_key ID番号のこと
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
