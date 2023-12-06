from .import views
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    path('sigup/', views.sigup, name='sigup'),
    path('sigin/', views.sigin, name='sigin'),
    path('sair/', views.sair, name='sair'),

    path('criar/post/', views.criar_post, name='criar_post'),
    path('criar/<int:post_id>/delete', views.deletar_post, name='deletar_post'), 

]
