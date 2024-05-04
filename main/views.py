from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import UserProfile, Notification, WorkOrder
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request, NotificationForm


def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'create_application.html', {'form': form})


def assign_master(request, request_id):
    if request.method == 'POST':
        request_instance = Request.objects.get(id=request_id)
        master_id = request.POST.get('master_id')
        master = UserProfile.objects.get(id=master_id)
        request_instance.assigned_master = master
        request_instance.save()

        notification = Notification.objects.create(user=master, message=f'Вы назначены на выполнение заявки "{request_instance.title}"')
        notification.save()

        return redirect('request_detail', request_id=request_id)
    else:
        masters = UserProfile.objects.filter(...)
        return render(request, 'assign_master.html', {'masters': masters})


def work_order_status(request, order_id):
    order = WorkOrder.objects.get(id=order_id)
    return render(request, 'work_order_status.html', {'order': order})


@receiver(post_save, sender=Request)
def create_request_notification(sender, instance, created, **kwargs):
    if created:
        NotificationForm.objects.create(user=instance.user, message="New request created.")


@receiver(post_save, sender=Request)
def create_status_change_notification(sender, instance, **kwargs):
    if instance.status_changed:
        NotificationForm.objects.create(user=instance.user, message="Request status changed.")


def notification_view(request):
    notifications = NotificationForm.objects.filter(user=request.user)
    return render(request, 'notifications.html', {'notifications': notifications})

