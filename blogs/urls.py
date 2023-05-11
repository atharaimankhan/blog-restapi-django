
from django.urls import path

from .views import BlogView, BlogsView

urlpatterns = [
    path('create/', BlogView.as_view()),
    path('<int:pk>/', BlogView.as_view()),
    path('update/', BlogView.as_view()),
    path('delete/<int:pk>', BlogView.as_view()),
    path('', BlogsView.as_view()),
    

]