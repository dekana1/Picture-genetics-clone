from django.db import models
from django.conf import settings
# Create your models here.


class TestTypes(models.Model):
    test_name = models.CharField(max_length=100)
    test_code = models.CharField(unique=True, max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.test_name


class Counselor(models.Model):
    counselor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=150)


class TestPurchase(models.Model):
    date_purchased = models.DateTimeField()
    test_info = models.ForeignKey(TestTypes, on_delete=models.CASCADE)
    test_status = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class GiftsPurchase(models.Model):
    test_purchase = models.ForeignKey(TestPurchase, on_delete=models.CASCADE)
    gift_code = models.CharField(max_length=100)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class OrderHistory(models.Model):
    StatusType = models.TextChoices('StatusType', 'Delivered Pending')
    date = models.DateTimeField()
    confirmation_id = models.CharField(unique=True, max_length=100)
    test = models.ForeignKey(TestTypes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_status = models.CharField(blank=True, choices=StatusType.choices, max_length=15)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Consult(models.Model):
    time_scheduled = models.DateTimeField()
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    test_to_be_discussed = models.ForeignKey(TestTypes, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
