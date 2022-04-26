from django.db import router
from django.urls import path,include
from django.contrib import admin
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# creating router object
router = DefaultRouter()

# Register StudentViewsSet with Router
router.register('studentapi',views.StudentViewSet,basename='StudentViewSet')

urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include(router.urls)),                  # given request to router urls
        path('gettoken/', TokenObtainPairView.as_view(),name='token_obtain_pair'),                 
        path('refreshtoken/', TokenRefreshView.as_view(),name='token_refresh'),                 
        path('verifytoken/', TokenVerifyView.as_view(),name='token_verify')                 
]