from django.urls import path 
from . import views
urlpatterns = [
    path("", views.api_overview, name="api_overview"),
    path("messages_list/", views.api_list, name="api_list"),
    path("message_create/", views.create_message, name="create_message"),
    path("message_delete/<str:pk>", views.delete_message, name="delete_message")
]