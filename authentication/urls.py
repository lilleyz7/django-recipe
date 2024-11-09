from django.urls import path
from .views import login_user, register_user, user_logout

urlpatterns = [
    path('login/', login_user),
    path('register/', register_user),
    path('logout/', user_logout),
]
