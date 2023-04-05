from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from.serializers import CommentSerializers

# Create your views here.


class CommentView(APIView):
     def post(self, request):
        serializer = CommentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)