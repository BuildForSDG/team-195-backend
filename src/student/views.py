from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentsSerializer

# A view to register, delete, view and update students details.


class studentsView(APIView):

    def post(self, request):

        """A method to register a student"""

        serializer = StudentsSerializer(data=request.data)

        # Checks if the request data is valid
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # Returns an error if one the request data is invlid
        return Response(serializer.errors, status=400)
