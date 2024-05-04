from django.urls import path
from .views import create_application, assign_master, work_order_status, notification_view

urlpatterns = [
    path('api/create/', create_application, name='home'),
    path('api/assign/', assign_master, name='assign_master'),
    path('work_order/<int:order_id>/', work_order_status, name='work_order_status'),
    path('notifications/', notification_view, name='notifications'),

]
