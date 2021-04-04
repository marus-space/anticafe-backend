from rest_framework import serializers

from .models import *


# AccountingEntry
class AccountingEntrySerializer(serializers.ModelSerializer):
    accounting_entry_type = serializers.SlugRelatedField(slug_field="name", queryset=AccountingEntryType.objects.all())

    class Meta:
        model = AccountingEntry
        fields = ('accounting_entry_id', 'client', 'accounting_entry_type', \
                  'date', 'cost_rub', 'cost_min', 'comment', )
        read_only_fields = ('date', )


# AccountingEntryType
class AccountingEntryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingEntryType
        fields = ('accounting_entry_type_id', 'name')


# Card
class CardSerializer(serializers.ModelSerializer):
    card_type = serializers.SlugRelatedField(slug_field="type", queryset=CardType.objects.all())

    class Meta:
        model = Card
        fields = ('card_id', 'card_type')


# CardStatus
class CardStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardStatus
        fields = ('card_status_id', 'status')


# CardType
class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardType
        fields = ('card_type_id', 'type')


# Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'last_name', 'first_name', 'patronymic', 'phone', \
                  'email', 'date_of_birth', 'balance_rub', 'balance_min', 'payment_min_status', \
                  'ban_status', 'ref_link_from', 'ref_link')
        read_only_fields = ('balance_rub', 'balance_min', 'ref_link')


# ClientCard
class ClientCardSerializer(serializers.ModelSerializer):
    card_status = serializers.SlugRelatedField(slug_field="status", queryset=CardStatus.objects.all())

    class Meta:
        model = ClientCard
        fields = ('client_card_id', 'client', 'card', 'card_status', 'date')
        read_only_fields = ('date', )


# ClientSubscription
class ClientSubscriptionSerializer(serializers.ModelSerializer):
    subscription = serializers.SlugRelatedField(slug_field="name", queryset=Subscription.objects.all())

    class Meta:
        model = ClientSubscription
        fields = ('client_subscription_id', 'client', 'subscription', 'start', 'end')
        read_only_fields = ('end', )


# Cost
class CostSerializer(serializers.ModelSerializer):
    cost_type = serializers.SlugRelatedField(slug_field="name", queryset=CostType.objects.all())

    class Meta:
        model = Cost
        fields = ('cost_id', 'client', 'cost_type', 'date', 'cost_rub', 'cost_min', 'bonus')
        read_only_fields = ('cost_id', 'client', 'cost_type', 'date', 'cost_rub', 'cost_min', 'bonus')


# CostType
class CostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostType
        fields = ('cost_type_id', 'name')


# ReferralSystem
class ReferralSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralSystem
        fields = ('client', 'num_of_invitees')
        read_only_fields = ('client', 'num_of_invitees', )


# Scan
class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ('scan_id', 'card', 'scaner_type', 'date')
        read_only_fields = ('scaner_type', )


# Subscription
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('subscription_id', 'name', 'start', 'end', 'duration', 'cost_rub')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visit_id', 'client', 'start', 'end', 'duration', 'comment')
        read_only_fields = ('duration', )


    # VisitTariff
class VisitTariffSerializer(serializers.ModelSerializer):
    card_type = serializers.SlugRelatedField(slug_field="type", queryset=CardType.objects.all())

    class Meta:
        model = VisitTariff
        fields = ('visit_tariff_id', 'card_type', 'start_tariff_zone', 'end_tariff_zone', 'cost_per_minute')
