from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from payments.models import Payment
from payments.serializers import PaymentSerializer, PaymentCreationSerializer
from payments.permissions import IsAdminPermission, IsAuthenticatedPermission


# Create your views here.
class PaymentListAPIView(ListAPIView):
    permission_classes = [IsAdminPermission]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @method_decorator(vary_on_headers("Authorization", ))
    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]

    @method_decorator(vary_on_headers("Authorization", ))
    @method_decorator(cache_page(60))
    def get(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = PaymentCreationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)
