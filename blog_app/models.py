from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Title: {self.title}; Author: {self.author.username};'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    description = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Description: {self.description}; Author: {self.author.username};'

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})


