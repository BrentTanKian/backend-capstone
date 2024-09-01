from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(ListCreateAPIView):
    """
    Handles GET (list all menu items) and POST (create a new menu item) requests.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """
    Handles GET (retrieve a single menu item), PUT (update a menu item),
    and DELETE (delete a menu item) requests.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    """
    A viewset that provides the standard actions for the Booking model.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer