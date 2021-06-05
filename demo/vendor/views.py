from vendor.serializers import VendSerializer
from vendor.models import Vendor
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class VendorView(APIView):

    def get(self, request, vendor_id, format=None):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        serializer = VendSerializer(vendor, many=False)
        return Response(serializer.data)

    # context={'request': request},
