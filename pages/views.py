from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import tasks
from .forms import Tasks
# Create your views here.


class Home(ListView):
    model = tasks
    template_name = 'pages/index.html'
    context_object_name = 'tasks'
    paginate_by = 5


class Detail(DetailView):
    model = tasks
    template_name = 'pages/detail.html'
    context_object_name = 'tasks'


class Post(CreateView):
    model = tasks
    template_name = 'pages/posts.html'
    fields = ['title', 'description', 'start', 'finish']
    success_url = '/'


class Delete_Post(DeleteView):
    model = tasks
    template_name = 'pages/delete.html'
    success_url = '/'


class UpdatePost(UpdateView):
    model = tasks
    fields = ['title', 'description', 'start', 'finish']
    template_name = 'pages/update.html'
    success_url = '/'
