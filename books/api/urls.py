from django.urls import path
from . import views


urlpatterns = [
    path('books', views.BookListCreateAPIView.as_view(), name='List_book'),
    path('books/<int:pk>', views.BookDetailAPIView.as_view(), name='Detail_book'),
    path('books/<int:book_id>/addcomment', views.CommentCreateAPIView.as_view(), name='add_comment'),
    path('comments/<int:pk>', views.CommentDetailAPIView.as_view(), name='Detail_comment'),
]
