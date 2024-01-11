from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# All messages are stored in memory for simplicity and are lost when the server is stopped.
messages = []

@api_view(['GET', 'POST'])
def message_list(request):
    """
    List all messages, or create a new message.
    """
    if request.method == 'GET':
        return Response(messages)

    elif request.method == 'POST':
        message = request.data
        messages.append(message)
        return Response(message, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, message_id):
    """
    Retrieve, update or delete a message.
    """
    if len(messages) <= message_id or message_id < 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(messages[message_id])

    elif request.method == 'PUT':
        messages[message_id] = request.data
        return Response(messages[message_id])

    elif request.method == 'DELETE':
        del messages[message_id]
        return Response(status=status.HTTP_204_NO_CONTENT)