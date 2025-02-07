from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actors_create_list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroiView.as_view(), name='actors_detail'),
    
]
