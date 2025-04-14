from django.urls import path

from .views import EntryListView, EntryUpdateView, EntryCreateView

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('create/', EntryCreateView.as_view(), name='entry_create'),
    path('update/', EntryUpdateView.as_view(), name='entry_update'),
]
