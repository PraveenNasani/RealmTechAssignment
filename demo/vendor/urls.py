from django.urls import include, path
from rest_framework import routers
from vendor import views


urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('vendor/<int:vendor_id>', views.VendorView.as_view())
]
