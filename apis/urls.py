from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views

from kautus.views import CustomAuthToken


urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('kautus.urls')),
  path('user/login', CustomAuthToken.as_view()),
   path('api-token-auth', views.obtain_auth_token)
]

