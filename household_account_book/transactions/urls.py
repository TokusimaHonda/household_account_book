from django.urls import path

from transactions import views

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("new/", views.transaction_new, name="transaction_new"),
    path("<int:transaction_id>/", views.transaction_detail, name="transaction_detail"),
    path("<int:transaction_id>/edit/", views.transaction_edit, name="transaction_edit"),
]