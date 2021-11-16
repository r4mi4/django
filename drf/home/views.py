from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Person
from .serializers import PersonSerializer


@api_view(['GET', 'POST'])
def one(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'name': f'My name is {name}'}, status=status.HTTP_200_OK)

    else:
        return Response({'name': 'My name is ramin'}, status=status.HTTP_100_CONTINUE)


# @api_view()
# def Persons(request):
#     persons = Person.objects.all()
#     ser_data = PersonSerializer(persons, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# @permission_classes([IsAdminUser])
# def person(request, id):
#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return Response({'err': 'user does not exist!'}, status=status.HTTP_404_NOT_FOUND)
#     ser_data = PersonSerializer(person)
#     return Response(ser_data.data, status=status.HTTP_200_OK)

#
# @api_view(['POST'])
# def person_create(request):
#     info = PersonSerializer(data=request.data)
#     if info.is_valid():
#         # Person(name=info.validated_data['name'], age=info.validated_data['age'],email=info.validated_data[
#         # 'email']).save()
#         info.save()
#         return Response({'messages': 'success'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
