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


class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]

    def get(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = PaymentCreationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)
