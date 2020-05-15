from rest_framework import serializers
from .models import Post, Comment



class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')


class PostSerializer(serializers.ModelSerializer):

    post_comments = serializers.HyperlinkedRelatedField(view_name='comment-detail', many=True, read_only=True)
    leave_comment = serializers.HyperlinkedIdentityField(view_name='comment-create')

    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'title', 'description', 
                  'created_date', 'post_comments', 'leave_comment',]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description',)


class CommentSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    author_link = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'author', 'author_link', 'description', 
                  'created_date',)



