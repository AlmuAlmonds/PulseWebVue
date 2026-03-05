from django.urls import path

from .views import admin_dashboard, dispatcher_dashboard, login_view, signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("dispatch/dashboard/", dispatcher_dashboard, name="dispatcher_dashboard"),
]