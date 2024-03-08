from .serializers import LivreSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livre


@api_view(['GET', 'POST'])
def user_ls(request, format=None):
    if request.method == 'GET':
        livres = Livre.objects.all()
        serializers = UserSerializers(users, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializers(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
