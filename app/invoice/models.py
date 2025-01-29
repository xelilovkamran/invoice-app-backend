from django.db import models
from account.models import CustomUser


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postCode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postCode}, {self.country}"


class Invoice(models.Model):

    PAYMENT_TERMS_CHOICES = [
        (1, 'Net 1 Day'),
        (7, 'Net 7 Days'),
        (14, 'Net 14 Days'),
        (30, 'Net 30 Days'),
    ]
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('draft', 'Draft'),
    ]

    identifier = models.CharField(
        max_length=6, unique=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    createdAt = models.DateField()
    paymentDue = models.DateField()
    description = models.CharField(max_length=255)
    paymentTerms = models.IntegerField(choices=PAYMENT_TERMS_CHOICES)
    clientName = models.CharField(max_length=100)
    clientEmail = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    senderAddress = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name='sender_address')
    clientAddress = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name='client_address')

    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.identifier


class Item(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name='items'
    )
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
