from django.urls import path
from .views import HomeView,CreateUserView, logout_view, LoginUserView
app_name= 'user'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginUserView.as_view(), name='login'),
]