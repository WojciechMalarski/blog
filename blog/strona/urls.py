from django.urls import path

from .views import HomeView, PostView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('post/delete_post/<int:pk>',DeletePostView.as_view(), name='delete_post'),


]

