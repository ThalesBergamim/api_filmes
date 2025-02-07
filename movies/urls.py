from django.urls import path  
from . import views 


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movies_create_list'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movies_detail'),
    
]
