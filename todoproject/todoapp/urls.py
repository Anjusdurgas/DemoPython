from django.urls import path, include

from todoapp import views
app_name='todoapp'
urlpatterns = [
    path('',views.index,name="index"),
    path('delete_task/<int:taskid>/',views.delete_task,name="delete_task"),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),
]