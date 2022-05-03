from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from users.models import BooksUser
from .serializers import FollowSerializer, UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    """
    CreateAPIView ensures only a create operation is possible
    """
    permission_classes = [AllowAny]
    queryset = BooksUser.objects.all()
    serializer_class = RegisterSerializer


# ------------------------------- Alternative-------------------------------- #
# Customize the create route (post)
# --------------------------------------------------------------------------- #

# class RegisterView(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer

#     # custom post implementation with custom JSON Response
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "message": "user created successfully!"
#         })

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "user created successfully!"
        })
