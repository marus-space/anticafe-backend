from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    last_name = serializers.CharField(max_length=45)
    first_name = serializers.CharField(max_length=45)
    patronymic = serializers.CharField(max_length=45)
    phone = serializers.DecimalField(max_digits=11, decimal_places=0)
    email = serializers.CharField(max_length=80)
    date_of_birth = serializers.DateField()
    balance_rub = serializers.DecimalField(max_digits=8, decimal_places=2)
    balance_min = serializers.DecimalField(max_digits=6, decimal_places=0)
    ref_link_from = serializers.CharField(max_length=8)
    ref_link = serializers.CharField(max_length=8)
    num_of_invitees = serializers.IntegerField()
    payment_min_status = serializers.IntegerField()
    ban_status = serializers.IntegerField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.balance_rub = validated_data.get('balance_rub', instance.balance_rub)
        instance.balance_min = validated_data.get('balance_min', instance.balance_min)
        instance.ref_link_from = validated_data.get('ref_link_from', instance.ref_link_from)
        instance.ref_link = validated_data.get('ref_link', instance.ref_link)
        instance.num_of_invitees = validated_data.get('num_of_invitees', instance.num_of_invitees)
        instance.payment_min_status = validated_data.get('payment_min_status', instance.payment_min_status)
        instance.ban_status = validated_data.get('ban_status', instance.ban_status)

        instance.save()
        return instance
