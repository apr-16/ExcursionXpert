from django.urls import path
from TravelApp.admin_views import IndexView,dist,place,package_details,pack_approve,pack_reject,View_bookings,history,guidee,view_pack,delete_pack,\
    pack_update

urlpatterns = [

    path('',IndexView.as_view()),
    path('dis',dist.as_view()),
    path('plc',place.as_view()),
    path('view',package_details.as_view()),
    path('approve',pack_approve.as_view()),
    path('reject',pack_reject.as_view()),
    path('bookings',View_bookings.as_view()),
    path('history',history.as_view()),
    path('guide',guidee.as_view()),
    path('view_pack',view_pack.as_view()),
    path('update',pack_update.as_view()),
    path('delete',delete_pack.as_view()),

    ]
def urls():
    return urlpatterns, 'admin', 'admin'