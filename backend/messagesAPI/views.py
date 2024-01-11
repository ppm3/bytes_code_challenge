import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Message
from .serializers import MessageSerializer


# Endpoints for Health Check and PING
@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint.
    """
    uptime = int(time.time())
    response_data = {
        'uptime': uptime
    }
    return Response(response_data)

@api_view(['GET'])
def ping(request):
    """
    Ping endpoint.
    """
    return Response('PONG')


#  MESSAGE CRUD
@api_view(['GET', 'POST'])
def message_list(request):
    """
    List all messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, message_id):
    """
    Retrieve, update or delete a message.
    """
    if message_id is None:
        return Response('Missing id', status=status.HTTP_400_BAD_REQUEST)

    # Get message by id or None if not found
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)