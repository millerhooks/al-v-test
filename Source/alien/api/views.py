from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from threat import *
from serializers import *
import time


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'IP Details': reverse('threat_details', request=request),
        })

class IPDetailsView(APIView):
    def get(self, request, *args, **kw):
        ip = request.GET.get('ip', "")
        details_request = IPDetails(ip, *args, **kw)

        result = DetailsSerializer(details_request)
        response = Response(result.data, status=status.HTTP_200_OK)

        return response
