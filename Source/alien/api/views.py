from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from threat import IPDetails, Reputation
from serializers import DetailsSerializer
from rest_framework import authentication, permissions
import time


class APIRoot(APIView):
    """
    API request for self details

    """

    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({
            'IP Details': reverse('threat_details', request=request),
        })

class IPDetailsView(APIView):
    """
    Get details for IP in URL querystring.

    example:
    http://localhost/api/v1/threat/details/69.43.161.174/

    """

    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kw):
        ip = request.GET.get('ip', "")
        details_request = IPDetails(ip, *args, **kw)

        result = DetailsSerializer(details_request)
        response = Response(result.data, status=status.HTTP_200_OK)

        return response
