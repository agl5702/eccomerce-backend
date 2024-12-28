from django.urls import path,include
from store.views import CategoryView,ProductView,OrderView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category',CategoryView, 'category')
router.register(r'product',ProductView, 'product')
router.register(r'order',OrderView, 'order')


urlpatterns = [
    path('',include(router.urls)),
]