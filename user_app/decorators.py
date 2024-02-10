from django.shortcuts import render
from django.db import models
from . models import *
from rest_framework.response import Response
from user_system.settings import SECRET_KEY, ALGORITHM
import traceback
import jwt
from functools import wraps

def authorizer(func):

    @wraps(func)
    def inner_func(request, *args, **kwargs):

        try:
            token = request.META['HTTP_AUTHORIZATION']
            if not token:
                return Response({'error': 'Token is missing'}, status=401)
            
            try:
                data = jwt.decode(token, SECRET_KEY, ALGORITHM)
                return func(request, *args, **kwargs)
            except jwt.exceptions.ExpiredSignatureError:
                return Response({'error': 'Session expired'}, status=401)
            except jwt.exceptions.InvalidTokenError:
                return Response({'error': 'Invalid token'}, status=400)

        except Exception as err:
            traceback.print_exc()
            return Response({'error': str(err)}, status=500)

    return inner_func


    