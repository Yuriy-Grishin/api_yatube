from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .permissions import AuthorAccess
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AuthorAccess]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Запрещено изменять чужой контент')
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Запрещено удалять чужой контент')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorAccess]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        author = self.request.user
        serializer.save(author=author, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_update(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Запрещено изменять чужой контент')
        serializer.save(author=self.request.user, post=post)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Запрещено удалять чужой контент')
        instance.delete()
