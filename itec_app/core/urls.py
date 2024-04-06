# from django.urls import path
# from django.views.generic import TemplateView
# from .views import PostDetail, UserAuth, UserCreate, LoginView

# app_name = 'itec_app'

# urlpatterns = [
    
# path('', TemplateView.as_view(template_name="index.html")),
# path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
# path('signup/', UserCreate.as_view(), name='usercreate'),
# # path('login/', LoginView.as_view(), name='userauth'),
# path('login/', UserAuth.as_view(), name='userauth'),
# # path('get/', PostDetail.as_view(), name='listget'),

# ]
from django.urls import re_path

from . import views

urlpatterns = [
    re_path('signup', views.signup),
    re_path('login', views.login),
    # re_path('test_token', views.test_token),
]