from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,\
    RetrieveUpdateAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from .permissions import IsAdminorStafforReadOnly, IsCommentOwnerorReadOnly
from .serializers import BookSerializer, CommentSerializer
from ..models import Book, Comment
from .pagination import SmallPagination, LargePagination


# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# Concrete view
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAdminorStafforReadOnly]
    pagination_class = SmallPagination


class BookDetailAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminorStafforReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_id')
        owner_of_comment_id = self.request.user.id
        check_comment = Comment.objects.filter(book_id=book_id, owner_of_comment_id=owner_of_comment_id)
        if check_comment.exists():
            raise ValidationError("You can make one comment for each book!")
        serializer.save(book_id=book_id, owner_of_comment_id=owner_of_comment_id)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerorReadOnly]
