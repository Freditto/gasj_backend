from django.urls import path
from .views import *

app_name = 'app1'
#
urlpatterns = [
    path('getGases/<int:user_id>', GetGases),
    path('resetGas/<int:gas_id>', ResetGas),
    path('insertGas', InsertGas),
    path('insertGasStatus', InsertGasStatus),
]
