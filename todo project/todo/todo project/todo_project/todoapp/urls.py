from .import views
from django.urls import path,include

urlpatterns = [

    path('',views.home,name='home'),
    path('home/<id>:id/',views.delete,name='delete'),
    path('edit/<id>:id/',views.edit,name='edit'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbdetailview/<int:pk>/',views.DetailView.as_view(),name='cbdetailview'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
    
]
