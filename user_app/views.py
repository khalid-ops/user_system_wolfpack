from user_app.models import CustomUser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.serializers import UserSerializer
import traceback
from user_system.settings import SECRET_KEY, ACCESS_TOKEN_LIFETIME, ALGORITHM
import jwt
from datetime import datetime
from .decorators import authorizer

@api_view(['POST'])
def register_user(request):

    try:
        user_data = request.data
        if user_data:
            
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                access_token = jwt.encode(
                    {
                    "user_id": serializer.data['id'],
                    "exp": datetime.utcnow() + ACCESS_TOKEN_LIFETIME,  
                    },
                    SECRET_KEY,
                    ALGORITHM
                )
                return Response({"user" : serializer.data, "accessToken" : access_token}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"message": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        traceback.print_exc()
        response_payload = {
            "message" : type(err).__name__
        }
        return Response(response_payload, 500)

@api_view(['POST'])
@authorizer
def login_user(request):

    try:
        login_data = request.data

        if CustomUser.objects.filter(email=login_data['email']).exists():
            user = CustomUser.objects.get(email=login_data['email'])
            serializer = UserSerializer(user)

            if serializer.data['password'] == login_data['password']:
                return Response({'message' : "User logged in!"}, 200)
            
            else:
                return Response({'message' : "Incorrect password!"}, 401)
        else:
            return Response({'message' : "User not found!"}, 404)

    except Exception as err:
        traceback.print_exc()
        response_payload = {
            "message" : type(err).__name__
        }
        return Response(response_payload, 500) 