from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q

from .serializers import *


# AccountingEntry
class AccountingEntryView(ListCreateAPIView):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer


class SingleAccountingEntryView(RetrieveUpdateDestroyAPIView):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer


# AccountingEntryType
class AccountingEntryTypeView(ListCreateAPIView):
    queryset = AccountingEntryType.objects.all()
    serializer_class = AccountingEntryTypeSerializer


class SingleAccountingEntryTypeView(RetrieveUpdateDestroyAPIView):
    queryset = AccountingEntryType.objects.all()
    serializer_class = AccountingEntryTypeSerializer


# Card
class CardView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class SingleCardView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# CardStatus
class CardStatusView(ListCreateAPIView):
    queryset = CardStatus.objects.all()
    serializer_class = CardStatusSerializer


class SingleCardStatusView(RetrieveUpdateDestroyAPIView):
    queryset = CardStatus.objects.all()
    serializer_class = CardStatusSerializer


# CardType
class CardTypeView(ListCreateAPIView):
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer


class SingleCardTypeView(RetrieveUpdateDestroyAPIView):
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer


# Client
class ClientView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        p = self.request.query_params.get('param')

        if p is not None:
            queryset = queryset.filter(Q(phone__icontains=p) | Q(last_name__icontains=p) | Q(first_name__icontains=p))
        return queryset


class SingleClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# ClientCard
class ClientCardView(ListCreateAPIView):
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer


class SingleClientCardView(RetrieveUpdateDestroyAPIView):
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer


# ClientSubscription
class ClientSubscriptionView(ListCreateAPIView):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer


class SingleClientSubscriptionView(RetrieveUpdateDestroyAPIView):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer


# Cost
class CostView(ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer


class SingleCostView(RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer


# CostType
class CostTypeView(ListCreateAPIView):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer


class SingleCostTypeView(RetrieveUpdateDestroyAPIView):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer


# Subscription
class SubscriptionView(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SingleSubscriptionView(RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# Visit
class VisitView(ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class SingleVisitView(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


# VisitTariff
class VisitTariffView(ListCreateAPIView):
    queryset = VisitTariff.objects.all()
    serializer_class = VisitTariffSerializer


class SingleVisitTariffView(RetrieveUpdateDestroyAPIView):
    queryset = VisitTariff.objects.all()
    serializer_class = VisitTariffSerializer

