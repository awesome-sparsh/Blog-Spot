from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:id>/', views.read_blog, name='post'),
    path('view-blogs/', views.view_blogs, name='view-blogs'),
    path('post-blog/', views.post_blog, name='view-blogs'),
    path('createNewBlog/', views.createNewBlog, name='createNewBlog'),
    path('post-blog/createNewBlog/', views.createNewBlog, name='createNewBlog'),
]