from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    model = Post # 使用するモデル
    paginate_by = 5 # 1ページに表示する件数
    ordering = ['-update_at'] # 記事の表示順をカスタマイズ
    template_name = 'blog/index.html'

class DetaiView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

class CretateView(generic.edit.CreateView):
    model = Post
    fields = '__all__' # ['title', 'text', 'author']
    template_name = 'blog/create.html'

class UpdateView(generic.edit.UpdateView):
    model = Post
    fields = '__all__' # ['title', 'text', 'author']
    template_name = 'blog/update.html'

class DeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/delete.html'