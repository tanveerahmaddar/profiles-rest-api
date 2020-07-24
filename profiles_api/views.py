from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test for HelloApiView."""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, delete)',
            'Is similar to a tradinal Django View',
            'GIves you the most control over yous application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview' : an_apiview})
