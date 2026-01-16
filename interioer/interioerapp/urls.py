from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
     path('home/', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('our_work/', views.our_workz,name='our_work'),

    # // admin side

    path('panel/', views.admins,name='admins'),
    path('del/<int:id>/', views.jasgd, name='delete'),
    path('update-status/<int:id>/<str:status_type>/', views.update_inquiry_status, name='update_status'),
    path('dels/<int:id>/', views.delsd, name='deletecontact'),
    path('adminlogin/', views.logins, name='login_page')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
