from rest_framework import pagination


class SmallPagination(pagination.PageNumberPagination):
    page_size = 3


class LargePagination(pagination.PageNumberPagination):
    page_size = 5
