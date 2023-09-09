from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('tasks/<int:pk>', views.Detail.as_view(), name='detail'),
    path('new/', views.Post.as_view(), name='new'),
    path('tasks/<int:pk>/delete', views.Delete_Post.as_view(), name='delete'),
    path('tasks/<int:pk>/update', views.UpdatePost.as_view(), name='update'),
]
