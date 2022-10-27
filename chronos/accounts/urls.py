from django.urls import path

from chronos.accounts import views


urlpatterns = [
    path('register/', views.register_account, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('show/', views.show_account, name='show'),
    path('edit/', views.edit_account, name='edit'),
    path('delete/', views.delete_account, name='delete'),

    # path('register/', RegisterView.as_view(), name='register profile'),
]
