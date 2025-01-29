from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serialzers import InvoiceSerializer
from .models import Invoice
from drf_spectacular.utils import extend_schema, extend_schema_view



class InvoiceListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InvoiceSerializer

    def get(self, request):
        invoices = request.user.invoice_set.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data

        invoice_serializer = InvoiceSerializer(data=data)

        if invoice_serializer.is_valid():
            invoice_serializer.save(author=request.user)
            return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InvoiceSerializer

    def get(self, request, pk):
        try:
            invoice = request.user.invoice_set.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({"error": "invoice did not find"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice = request.user.invoice_set.get(pk=pk)
        data = request.data

        serializer = InvoiceSerializer(invoice, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            invoice = request.user.invoice_set.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({"error": "invoice did not find"}, status=status.HTTP_404_NOT_FOUND)

        sender_address = invoice.senderAddress
        client_address = invoice.clientAddress

        sender_address.delete()
        client_address.delete()
        return Response({"success": "invoice deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
