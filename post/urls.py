from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('post/<int:pk>', views.get_post, name='view_post'),
    path('post/create', views.create_post_form, name='create_post'),
    path('post/<int:pk>/update', views.update_post, name='update_post'),
    path('post/<int:pk>/delete', views.delete_post, name='delete_post'),
]