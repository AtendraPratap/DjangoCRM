from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', lead_create, name='lead-create'),
    # path('email/', send_email, name='send-email'), ----> (FOR EMAIL, NIU)
]