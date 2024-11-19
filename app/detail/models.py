from django.db import models
from django.utils import timezone


class OTP(models.Model):
    otp = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        return self.expiration_time < timezone.now()

    def __str__(self):
        return self.otp
