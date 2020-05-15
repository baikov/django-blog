from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .utils import get_toc

from .models import Post, PostImages


class PostListView(ListView):
    template_name = 'blog/blog-list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        posts = Post.objects.all()
        limit = 10
        if not self.request.user.is_superuser:
            posts = posts.published()
        return posts.order_by('-is_highlighted', '-created_date')[:limit]

    def get_context_data(self,**kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        featured_posts = Post.objects.featured()


        if self.request.user.is_superuser:
            context['featured'] = featured_posts
        else:
            context['featured'] = featured_posts.published()
        return context

    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     limit = 10
    #     return posts.published()[:limit]
        # posts_featured = Post.objects.featured()
        # if not self.request.user.is_superuser:
        #     posts = posts.published()
        #     posts_featured = posts_featured.published()
            
        # context['last_posts'] = posts[:limit]
        # context['last_posts_featured'] = posts_featured[:limit]
        # return context
        #return Post.objects.order_by('-updated_date')[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = 'Sart'
        if self.object.is_toc:
            context['toc'] = get_toc(self.object.body, self.object.toc_depth)
        # context['images'] = PostImages.objects.filter(post=self.object)
        context['images'] = self.object.images.all()
        return context

class PostEditView(UpdateView):
    model = Post
    fields = ['title','slug', 'is_published', 'is_highlighted', 'is_toc', 'toc_depth', 'short_text', 'body', 'seo_title', 'seo_description']
    template_name_suffix = '_update_form'

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

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    images = PostImages.objects.filter(post=post)
    # images = post.images.all()
    context = {'post': post, 'images': images}
    return render(request, 'blog/blog-detail.html', context)
'''
