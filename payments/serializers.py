from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentCreationSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        payment = Payment.create_payment(**validated_data)
        payment.save()
        return payment

    subscription_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    time_amount = serializers.IntegerField(min_value=1)
