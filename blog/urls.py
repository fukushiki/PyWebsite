from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 一覧表示のURL
    path('', views.IndexView.as_view(), name='index'),

    # 新規作成のURL
    path('post/create/', views.CretateView.as_view(), name='create'),

    # 記事ID
    path('post/<int:pk>', views.DetaiView.as_view(), name='detail'),

    # 内容更新のURL
    path('post/<int:pk>/update', views.UpdateView.as_view(), name='update'),

    # 記事削除のURL
    path('post/<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
]