from django.urls import path

from chronos.accounts import views


urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('login/', views.login_user, name='login_account'),
    path('logout/', views.logout_user, name='logout_account'),
    path('show/', views.show_account, name='show_account'),
    path('edit/', views.edit_account, name='edit_account'),
    path('delete/', views.delete_account, name='delete_account'),

    # path('register/', RegisterView.as_view(), name='register profile'),
]
