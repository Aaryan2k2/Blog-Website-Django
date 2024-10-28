from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name="blog-home"),
    path('about/',views.about,name='blog-about'),
    path('<int:blog_id>/detail/',views.PostDetailView,name='blog-detail'),
    path('post/create/',views.post_create,name='blog-create'),
    path('<int:blog_id>/post/edit',views.post_edit,name='blog-edit'),
    path('<int:blog_id>/post/delete',views.post_delete,name='blog-delete'),
    path('user/<str:username>/',views.user_posts,name='user-posts'),
    path('<int:blog_id>/comment',views.comments,name="comment"),    
    path('<int:comment_id>/comment_delete/',views.comment_delete,name="comment-delete"),    
]