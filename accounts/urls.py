from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = {
    path('register/', views.UserRegstrationView.as_view(),
         name='user_registration'),
}
