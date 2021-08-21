from django.http import request
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, User, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        read_only_fields = ('pub_date',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('created',)
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username')
        model = User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description')
        read_only_fields = ('id',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only = True,
        default=serializers.CurrentUserDefault()    
    )
    following = serializers.SlugRelatedField(slug_field ='username', queryset=User.objects.all())

    def validate(self, data):
            if self.context['request'].user == data['following']:
                raise serializers.ValidationError('Вы не можете подписаться на себя.')
            return data
    class Meta:
        fields = ('user', 'following',)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=('Вы уже подписаны.')
            )
        ]

