from django.urls import path, include
from .views import all_blogs
from . import views
app_name ='blog'

urlpatterns = [

    path('', all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]