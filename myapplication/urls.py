from django.urls import path
from myapplication import views

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('update/<int:id>',views.userupdate,name='update'),
    path('delete/<int:id>',views.user_delete,name='delete')              
]
