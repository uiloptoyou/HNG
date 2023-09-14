from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(),
         name='person-retrieve-update-destroy')
]
