from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 15
    page_query_param = 'page_size'
    max_page_size = 100


class SubjectPaginator(PageNumberPagination):
    page_size = 15
    page_query_param = 'page_size'
    max_page_size = 100
