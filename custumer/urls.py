from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=format_suffix_patterns([
    path('register/admin/', ListCreat.as_view(),name='registers'),
    path('list/admin/<int:pk>/', ListCreatDetail.as_view(),name='registera'),
    path('list/agent/', RecensementView.as_view(),name='registera'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
])