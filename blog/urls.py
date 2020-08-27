from django.urls import path
from .views import HomeView, PostDetailView, CreateNewPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-details"),
    path('add_post/', CreateNewPostView.as_view(), name="add-post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="edit-post"),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name="delete-post"),
]
