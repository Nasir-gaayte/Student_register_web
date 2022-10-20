from django.urls import path
from . import views
from .views import Add_studentView,AllDetailView

urlpatterns = [
    path('',views.home,name='home'),
    path('add_student/',views.Add_studentView.as_view(),name='add_student'),
    path('detail/',views.AllDetailView.as_view(), name='detail'),
    # path('detail_id/<pk>/',views.AboutStudent.as_view(),name='detail_id'),
    path('detail_id/<int:pk>/',views.aboutstudent,name='detail_id'),
]
