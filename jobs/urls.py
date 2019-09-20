from django.urls import path
from . import views
app_name = 'jobs'

urlpatterns= [
    path('', views.search, name='search'),
    path('past_job/', views.past_job, name='past_job'),
]