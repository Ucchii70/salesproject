from django.urls import path

from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('list', permanent=False)),  # ルートURLをリダイレクト
    path('list/', views.SalesListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.SalesDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SalesUpdateView.as_view(), name='update'),
    path('create/', views.SalesCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.SalesDeleteView.as_view(), name='delete'),
    path('manager-check/<int:pk>/', views.manager_check, name='manager-check'),
    path('list2/', views.listview, name='list2'),
]