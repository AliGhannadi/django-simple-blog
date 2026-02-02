from django.urls import path
from .views import login_view, register_view, logout_view
app_name = 'accounts'
urlpatterns = [
    # registration / signup
    path('register/', register_view, name="sign_up"),
    # login
    path('login/', login_view, name="login"),
    # logout
    path('logout/', logout_view, name="logout")
    
]