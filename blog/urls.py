from .import views
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    
    path('criar', views.criar, name='criar'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),

    path('signin/', views.signin, name='signin'),
    path('sair/', views.sair, name='sair')
]
