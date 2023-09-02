from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.adminlog.as_view(), name='login'),
    path('showprofile/', views.show_profile, name='showprofile'),
    path('logout/', views.log_out.as_view(), name='logout'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('profile/', views.profile, name='profile'),

    # URL for user login
    # path('profile/edit/', views.profile_edit, name='profile_edit'),  # URL for profile editing
]
