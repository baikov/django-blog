from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post

class ListView(generic.ListView):
    template_name = 'blog/blog-list.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-updated_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = 'Sart'
        return context

def index(request):
    homepage_post_list = Post.objects.order_by('-updated_date')[:5]
    context = {'post_list': homepage_post_list}
    return render(request, 'blog/index.html', context)

'''
def blog_list(request):
    latest_post_list = Post.objects.order_by('-updated_date')[:5]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'blog/blog-list.html', context)

def blog_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {'post': post}
    return render(request, 'blog/blog-detail.html', context)

'''