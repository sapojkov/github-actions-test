from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GreetingSerializer


class GreetingView(APIView):

    def get(self, request):
        data = {"message": "Hello, welcome to the API!"}
        serializer = GreetingSerializer(data)
        return Response(serializer.data)
