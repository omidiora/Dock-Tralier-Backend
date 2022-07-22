from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,  DocksItemViews
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('send', DocksItemViews.as_view() ,name='aaa')
]