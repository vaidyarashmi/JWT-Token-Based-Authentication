from django.urls import path,include
from testapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)
from rest_framework.authtoken import views
urlpatterns = [
    path('',include(router.urls)),
    path('get_api_token',views.obtain_auth_token,name='get-api-token'),
]
