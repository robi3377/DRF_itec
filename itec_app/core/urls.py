from django.urls import path
from django.views.generic import TemplateView
from .views import PostDetail, UserAuth, UserCreate

app_name = 'itec_app'

urlpatterns = [
    
path('', TemplateView.as_view(template_name="index.html")),
path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
path('signup/', UserCreate.as_view(), name='usercreate'),
path('login/', UserAuth.as_view(), name='userauth'),
# path('get/', PostDetail.as_view(), name='listget'),

]