from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from TravelApp.views import indexview,registration,Login,package_details
from TravelApp import admin_urls, user_urls

urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    # path('staff/',staff_urls.urls()),
    # path('member/',member_urls.urls()),

    path('',indexview.as_view()),
    path('packd',package_details.as_view()),
    path('register',registration.as_view()),
    path('login',Login.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)