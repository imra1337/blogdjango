from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]
