from rest_framework import serializers

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'last_name', 'first_name', 'patronymic', 'phone', \
                  'email', 'date_of_birth', 'balance_rub', 'balance_min', 'ref_link_from', \
                  'ref_link', 'num_of_invitees', 'payment_min_status', 'ban_status')
