from rest_framework import serializers


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
