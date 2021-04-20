from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import UserSerializer
from .models import User_data
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.



class CreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class retrieveViewSet(generics.ListAPIView):
    queryset = User_data.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def retrieve_data(requset):
    users = User_data.objects.all()
    serializer = UserSerializer(users, many=True)
    info = {'Status':True, 'Message':'All user inforation' ,'Data': serializer.data}
    return Response(info)