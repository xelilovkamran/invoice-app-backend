from .models import Invoice, Address, Item
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'postCode', 'country']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'price', 'total']


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    senderAddress = AddressSerializer()
    clientAddress = AddressSerializer()

    class Meta:
        model = Invoice
        fields = ['id', 'identifier', 'createdAt', 'paymentDue',
                  'description', 'paymentTerms', 'clientName', 'clientEmail', 'status', 'items', 'total', 'senderAddress', 'clientAddress']
        read_only_fields = ['id']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sender_address_data = validated_data.pop('senderAddress')
        client_address_data = validated_data.pop('clientAddress')

        sender_address = Address.objects.create(**sender_address_data)
        client_address = Address.objects.create(**client_address_data)
        invoice = Invoice.objects.create(
            senderAddress=sender_address, clientAddress=client_address,  **validated_data)
        for item_data in items_data:
            item = Item.objects.create(owner=invoice, **item_data)

        return invoice

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        sender_address_data = validated_data.pop('senderAddress')
        client_address_data = validated_data.pop('clientAddress')

        sender_address = instance.senderAddress
        client_address = instance.clientAddress

        sender_address.street = sender_address_data.get(
            'street', sender_address.street)
        sender_address.city = sender_address_data.get(
            'city', sender_address.city)
        sender_address.postCode = sender_address_data.get(
            'postCode', sender_address.postCode)
        sender_address.country = sender_address_data.get(
            'country', sender_address.country)
        sender_address.save()

        client_address.street = client_address_data.get(
            'street', client_address.street)
        client_address.city = client_address_data.get(
            'city', client_address.city)
        client_address.postCode = client_address_data.get(
            'postCode', client_address.postCode)
        client_address.country = client_address_data.get(
            'country', client_address.country)
        client_address.save()

        instance.createdAt = validated_data.get(
            'createdAt', instance.createdAt)
        instance.paymentDue = validated_data.get(
            'paymentDue', instance.paymentDue)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.paymentTerms = validated_data.get(
            'paymentTerms', instance.paymentTerms)
        instance.clientName = validated_data.get(
            'clientName', instance.clientName)
        instance.clientEmail = validated_data.get(
            'clientEmail', instance.clientEmail)
        instance.status = validated_data.get('status', instance.status)
        instance.total = validated_data.get('total', instance.total)
        instance.save()

        items = Item.objects.filter(owner=instance)

        for item in items:
            item.delete()

        for item_data in items_data:
            item = Item.objects.create(owner=instance, **item_data)

        return instance