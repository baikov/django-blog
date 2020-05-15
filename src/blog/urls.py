from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.PostEditView.as_view(), name='edit'),
    # path('<slug:slug>/', views.blog_detail, name='detail'),
]