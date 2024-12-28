from django.urls import path
from user.api.api import user_api_view, user_detail_api_view,get_user_info_by_email

urlpatterns = [
    path('user/', user_api_view, name='usuario_api'),
    path('user/<int:pk>/',user_detail_api_view, name='user_detail_api_view'),
    path('verify-user/',get_user_info_by_email, name='verify_user_email'),
]