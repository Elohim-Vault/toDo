
from django.urls import path, include
from .views import taskList, newTask, detailTask, editTask, deleteTask, changeStatus

urlpatterns = [
    path('', taskList, name='task-list'),
    path('newtask', newTask, name="new-task"),
    path('edit/<int:pk>', editTask, name="edit-task"),
    path('task/<int:pk>', detailTask, name="detail-task"),
    path('delete/<int:pk>', deleteTask, name="delete-task"),
    path('changestatus/<int:pk>/', changeStatus, name="change-status"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]