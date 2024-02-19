from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path("users/<int:pk>/", views.UserDetailUpdateDeleteView.as_view(),
         name="users-detail"),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]
