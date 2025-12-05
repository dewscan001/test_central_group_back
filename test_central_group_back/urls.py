"""
URL configuration for test_central_group_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from product.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('product', get_all_products),
    path('product/add', post_product),
    path('promotion', get_all_promotion),
    path('promotion/add', post_promotion),
    path('product/<int:id>', get_product_by_id),
    path('promotion/<int:id>', get_promotion_by_id),
    path('product/edit/<int:id>', put_product_by_id),
    path('promotion/edit/<int:id>', put_promotion_by_id),
    path('product/delete/<int:id>', delete_product_by_id),
    path('promotion/delete/<int:id>', delete_promotion_by_id)
]
