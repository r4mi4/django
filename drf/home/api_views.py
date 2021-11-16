from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ModelViewSet
class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    
# ViewSet
# class PersonViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Person.objects.all()
#         serializer = PersonSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Person.objects.all()
#         person = get_object_or_404(queryset, pk=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'ok'})
#         else:
#             return Response(serializer.errors)
