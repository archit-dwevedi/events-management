



from django.urls import path

from event.api.views import api_event_create_view
from event.api.views import (
    api_event_detail_slug_view,
    api_delete_event_view,
    ApiEventListView,
    api_event_invite_view,
    api_event_accept_invite_view
)

app_name = 'event'


urlpatterns = [
    path('list', ApiEventListView.as_view(), name="list"),
    path('invite/<str:slug>',api_event_invite_view, name = "event_invite"),
    path('accept_invite',api_event_accept_invite_view, name = "event_accept"),
    path('create', api_event_create_view, name = "event_create"),
    path('delete/<str:slug>', api_delete_event_view, name = "event_delete"),
    path('<str:slug>', api_event_detail_slug_view, name = "event_detail"),
]
