from django.urls import path
from .views import (PostListView, 
                    PostCreateView, 
                    PostDetailView,
                    CommentCreateView,
                    CommentDetailView
                    # assign_task
                    )

urlpatterns = [
    path('', PostListView.as_view(),
         name='posts'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/comment-create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    # path('<int:pk>/assign/', assign_task, name='task-assign'),
]