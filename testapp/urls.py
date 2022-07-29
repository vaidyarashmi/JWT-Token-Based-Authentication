from django.urls import path,include
from testapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV)
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    path('',include(router.urls)),
    path('get_api_token',views.obtain_auth_token,name='get-api-token'),
    path('auth-jwt-obtain/',obtain_jwt_token),
    path('auth-jwt-refresh/',refresh_jwt_token),
    path('auth-jwt-verify/',verify_jwt_token),
]
