from rest_framework import generics, permissions, authentication
from .serializers import OrderItemSerializer
from .models import OrderItem


class OrderItemApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(order_id__customer_id=self.request.user)


class OrderItemDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem

    def get_queryset(self):
        from time import sleep
        return super().get_queryset()
