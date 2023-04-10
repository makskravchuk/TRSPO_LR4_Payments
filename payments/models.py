from django.db import models


class Payment(models.Model):
    subscription_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_payment(subscription_id, price, time_amount):
        amount = price * time_amount
        payment = Payment(subscription_id=subscription_id, amount=amount)
        return payment
