from django.urls import path
from . import views
urlpatterns = [
    path('',views.StandardListView.as_view(),name='standard_list'),
    path('<slug:slug>/',views.SubjectListView.as_view(),name='subject_list'),
]