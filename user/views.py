from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .filter import CarListingFilter, ProductFilter, ContactFilter
from .models import CarListing, UserProfile, Product, Contact
from .serializers import CarListingSerializer, UserProfileSerializer, ProductSerializer, ContactSerializer
from django.contrib.auth import logout
from rest_framework.response import Response


class UserLogIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = Token.objects.get(user=user)
        return Response({"token": token.key, "id": user.pk, "email": user.email})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Returns the permission based on the type of action"""

        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-create_date")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by("-create_date")
    serializer_class = ContactSerializer
    filterset_class = ContactFilter

class CarListingViewSet(viewsets.ModelViewSet):
    queryset = CarListing.objects.all().order_by("-ppc_score")
    serializer_class = CarListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarListingFilter


def car_listing_search(request):
    if request.method == "GET":
        # Get query parameters from the URL
        queryset = CarListing.objects.all().order_by("-ppc_score")
        seriliser = CarListingSerializer(queryset, many=True)

        return render(request, "index.html", {"search_results": seriliser.data})
    else:
        return render(request, "index.html", {"search_results": []})
