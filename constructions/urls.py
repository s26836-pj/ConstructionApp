from django.urls import path
from .views import ConstructionListView, ConstructionCreateView, ConstructionUpdateView, \
     ConstructionArchiveView

urlpatterns = [
    path('', ConstructionListView.as_view(), name='construction_list'),
    path('new/', ConstructionCreateView.as_view(), name='construction_create'),
    path('<int:pk>/update/', ConstructionUpdateView.as_view(), name='construction_update'),
    path('<int:pk>/archive/', ConstructionArchiveView.as_view(), name='construction_archive'),
]
