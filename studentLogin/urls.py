from django.urls import path
from . import views

urlpatterns = [
    path('login_Student', views.login_user, name ="login"),
    path('logout_Student', views.logout_user, name='logout'),
    path('register_Student', views.register_user, name='register_user'),

    path("advisorRegister", views.advisor_registration, name="advisorRegister"),
    path('advisorLogin', views.advisor_login, name='advisorLogin'),
    path('advisorLogout', views.advisor_logout, name='advisorLogout'),
    path('adminLogin', views.admin_login, name='adminLogin'),
    path('adminLogout', views.admin_logout, name='adminLogout'),
]

