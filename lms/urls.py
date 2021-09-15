from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
