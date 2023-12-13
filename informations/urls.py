
from django.contrib import admin
from django.urls import path
from .views import InformationList,InformationDetail

urlpatterns = [
    path("",InformationList.as_view(),name="list_info"),
    path("<uuid:pk>/",InformationDetail.as_view(),name="info_details")
]
