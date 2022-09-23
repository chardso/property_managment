from rest_framework.routers import SimpleRouter
from django.urls import path

from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet 

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')
# routes.register(r'user/<user_pk>/upassword', UserViewSet, basename='user-update-password')

urlpatterns = [
    *routes.urls,
]