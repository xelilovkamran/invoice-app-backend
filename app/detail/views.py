from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from detail.models import OTP

from django.core.mail import send_mail

import random
from django.utils import timezone
from django.http import HttpRequest
from django.conf import settings


@api_view(['POST',])
def send_otp(request: HttpRequest):
    email = request.data.get('email')
    if not email:
        return Response({'message': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

    otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])

    try:
        send_mail(
            'Email Verification OTP',
            f'Your OTP for email verification is: {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        return Response({'message': f'Error sending OTP: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    otp_obj = OTP.objects.create(otp=otp,
                                 expiration_time=timezone.now() + timezone.timedelta(minutes=180))
    return Response({'message': 'OTP sent to the email address', 'otp_id': otp_obj.pk, 'otp': otp}, status=status.HTTP_200_OK)


@api_view(['POST',])
def check_otp(request):
    otp_entered = request.data.get('otp')
    otp_id = request.data.get('otp_id')

    if not (otp_entered and otp_id):
        return Response({'message': 'Phone number, OTP, and OTP ID are required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        otp_obj = OTP.objects.get(
            pk=otp_id, otp=otp_entered)
    except OTP.DoesNotExist:
        return Response({'message': 'OTP not found'}, status=status.HTTP_404_NOT_FOUND)

        # Verify the OTP
    if str(otp_entered) != otp_obj.otp:
        return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if OTP is expired
    if otp_obj.is_expired():
        return Response({'message': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

    if str(otp_entered) == otp_obj.otp:
        otp_obj.delete()  # Delete OTP object after successful verification
        return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
