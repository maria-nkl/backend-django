from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleByCategoryListView,\
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView, CommentCreateView, \
    ArticleByTagListView, ArticleSearchResultView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('articles/create/', ArticleCreateView.as_view(), name='articles_create'),
    path('articles/<str:slug>/update/', ArticleUpdateView.as_view(), name='articles_update'),
    path('articles/<str:slug>/delete/', ArticleDeleteView.as_view(), name='articles_delete'),
    path('articles/<str:slug>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('articles/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
    path('articles/tags/<str:tag>/', ArticleByTagListView.as_view(), name='articles_by_tags'),
    path('category/<str:slug>/', ArticleByCategoryListView.as_view(), name="articles_by_category"),
    path('search/', ArticleSearchResultView.as_view(), name='search'),
]