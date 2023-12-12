from django.urls import path
from TravelApp.user_views import IndexView,package_details,viewconfirm,viewbooking,pay,guidee

urlpatterns = [

    path('',IndexView.as_view()),
    path('packd',package_details.as_view()),
    path('viewconfirm',viewconfirm.as_view()),
    path('viewbooking',viewbooking.as_view()),
    path('payment',pay.as_view()),
    path('guide',guidee.as_view()),
    
    


    
    ]
def urls():
    return urlpatterns, 'user', 'user'