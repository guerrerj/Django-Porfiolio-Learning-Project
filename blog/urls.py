from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.blogIndex, name="blogIndex"), 
    path("<int:id>", views.blogDetail, name="blogDetail"),
    path("<category>/", views.blogCategory, name="blogCategory")     
]