from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField
from djoser.serializers import UserSerializer


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


class CustomUserSerializer(UserSerializer):

    class Meta:
        fields = ('username', 'first_name', 'last_name')
        model = User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description')
        read_only_fields = ('id',)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field ='username', queryset=User.objects.all())

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(
            user=self.context['request'].user,
            following = user  
        )
        if user == self.context['request'].user:
            raise serializers.ValidationError("Вы не можете подписаться на самого себя.")
        if follow is True:
            raise serializers.ValidationError("Вы уже подписаны.")
        return data

    class Meta:
        fields = ('user', 'following',)
        model = Follow
