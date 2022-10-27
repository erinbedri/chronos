from django.urls import path

from chronos.watches import views

urlpatterns = [
    path('add/', views.add_watch, name='add_watch'),
    path('all/', views.show_all_watches, name='show_all_watches'),
    path('collection/', views.show_my_watches, name='show_collection'),
    path('details/<int:pk>', views.show_watch, name='show_watch'),
    path('edit/<int:pk>', views.edit_watch, name='edit_watch'),
    path('delete/<int:pk>', views.delete_watch, name='delete_watch'),
    path('like/<int:pk>', views.like_watch, name='like_watch'),
]
