


from django.contrib import admin
from django.urls import path

#Our Imports
from django.urls import include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/event/', include('event.api.urls')),
    path('api/account/', include('account.api.urls')),

]
