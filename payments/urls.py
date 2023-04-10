from django.urls import path

from payments.views import PaymentAPIView, PaymentListAPIView

urlpatterns = [path("payments/", PaymentListAPIView.as_view()),
               path("create-payment/", PaymentAPIView.as_view()),
               path("payment/<int:pk>", PaymentAPIView.as_view()), ]
