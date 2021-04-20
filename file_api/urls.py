from django.urls import path
from .views import CreateView, retrieveViewSet, retrieve_data

urlpatterns = [
    path('create/', CreateView.as_view(), name='file-upload'),
    path('list/', retrieveViewSet.as_view(), name='list'),
    path('retrieve/',retrieve_data, name='store'),
]