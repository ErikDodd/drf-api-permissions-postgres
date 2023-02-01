from django.urls import path
from .views import ShoeList, ShoeDetail

urlpatterns = [
    path("", ShoeList.as_view(), name="shoe_list"),
    path("<int:pk>/", ShoeDetail.as_view(), name="shoe_detail"),
]
