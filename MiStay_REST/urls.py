


from django.contrib import admin
from django.urls import path

#Our Imports
from django.urls import include
from account.api.views import index




urlpatterns = [
    path('api',index, name= "index_api"),
    path('admin/', admin.site.urls, name = "admin_views"),
    path('api/event/', include('event.api.urls'), name= "event_apis"),
    path('api/account/', include('account.api.urls'), name= "account_apis"),
]
