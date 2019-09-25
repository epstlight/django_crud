from django.urls import path
from . import views

app_name = 'articles'

urlpatterns= [
    # 입력 페이지 제공
    # path('new/', views.new, name='new'),
    # 데이터를 전달받아서 article 생성
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'), # detatil
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
]