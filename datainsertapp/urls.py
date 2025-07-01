from django.urls import path
from datainsertapp import views

urlpatterns = [
    path('',views.data,name='data'),
    path('view',views.viewdata,name='viewdata'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),



    
]