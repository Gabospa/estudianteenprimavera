from django.urls import path
import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<uuid:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<uuid:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentList.as_view(), name='comments-list'),
    path('comments/<uuid:pk>/', views.CommentDetail.as_view(), name='comments-detail'),
]