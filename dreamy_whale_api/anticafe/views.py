from django.db import OperationalError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
import string
import random

from .serializers import *


# AccountingEntry
class AccountingEntryView(ListCreateAPIView):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer

    def get_queryset(self):
        queryset = AccountingEntry.objects.all().order_by('-date')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleAccountingEntryView(RetrieveUpdateDestroyAPIView):
    queryset = AccountingEntry.objects.all()
    serializer_class = AccountingEntrySerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# AccountingEntryType
class AccountingEntryTypeView(ListCreateAPIView):
    queryset = AccountingEntryType.objects.all()
    serializer_class = AccountingEntryTypeSerializer


class SingleAccountingEntryTypeView(RetrieveUpdateDestroyAPIView):
    queryset = AccountingEntryType.objects.all()
    serializer_class = AccountingEntryTypeSerializer


# Calculator
class CalculatorView(ListCreateAPIView):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer

    def get_queryset(self):
        queryset = Calculator.objects.all().order_by('-calculator_id')
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            super(ListCreateAPIView, self).create(request, *args, **kwargs)
            queryset = Calculator.objects.last()
            serializer = CalculatorSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# Card
class CardView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleCardView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


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
        queryset = Client.objects.all().order_by('-client_id')
        p = self.request.query_params.get('param')
        if p is not None:
            queryset = queryset.filter(Q(phone__icontains=p) | Q(last_name__icontains=p) | Q(first_name__icontains=p))
        return queryset

    def perform_create(self, serializer):
        ref_link = ref_generator()
        while Client.objects.all().filter(ref_link=ref_link):
            ref_link = ref_generator()
        return serializer.save(ref_link=ref_link)

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


def ref_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class SingleClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# ClientCard
class ClientCardView(ListCreateAPIView):
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer

    def get_queryset(self):
        queryset = ClientCard.objects.all().order_by('-date')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleClientCardView(RetrieveUpdateDestroyAPIView):
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# ClientSubscription
class ClientSubscriptionView(ListCreateAPIView):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer

    def get_queryset(self):
        queryset = ClientSubscription.objects.all().order_by('-client_subscription_id')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleClientSubscriptionView(RetrieveUpdateDestroyAPIView):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# Cost
class CostView(ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

    def get_queryset(self):
        queryset = Cost.objects.all().order_by('-date')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleCostView(RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# CostType
class CostTypeView(ListCreateAPIView):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer


class SingleCostTypeView(RetrieveUpdateDestroyAPIView):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer


# Questionnaire
class QuestionnaireView(ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        queryset = Questionnaire.objects.all().order_by('-questionnaire_id')
        return queryset

    def perform_create(self, serializer):
        ref_link = ref_generator()
        while Questionnaire.objects.all().filter(ref_link=ref_link):
            ref_link = ref_generator()
        return serializer.save(ref_link=ref_link)

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleQuestionnaireView(RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# ReferralSystem
class ReferralSystemView(ListCreateAPIView):
    queryset = ReferralSystem.objects.all()
    serializer_class = ReferralSystemSerializer

    def get_queryset(self):
        queryset = ReferralSystem.objects.all().order_by('-client_id')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleReferralSystemView(RetrieveUpdateDestroyAPIView):
    queryset = ReferralSystem.objects.all()
    serializer_class = ReferralSystemSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# ReservationObject
class ReservationObjectView(ListCreateAPIView):
    queryset = ReservationObject.objects.all()
    serializer_class = ReservationObjectSerializer


class SingleReservationObjectView(RetrieveUpdateDestroyAPIView):
    queryset = ReservationObject.objects.all()
    serializer_class = ReservationObjectSerializer


# Reservation
class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        queryset = Reservation.objects.all().order_by('-start')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleReservationView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# ReservationTariff
class ReservationTariffView(ListCreateAPIView):
    queryset = ReservationTariff.objects.all()
    serializer_class = ReservationTariffSerializer


class SingleReservationTariffView(RetrieveUpdateDestroyAPIView):
    queryset = ReservationTariff.objects.all()
    serializer_class = ReservationTariffSerializer


# Scan
class ScanView(ListCreateAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

    def get_queryset(self):
        queryset = Scan.objects.all().order_by('-date')
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleScanView(RetrieveUpdateDestroyAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self):
        queryset = Visit.objects.all().order_by('-visit_id')
        c = self.request.query_params.get('client')
        if c is not None:
            queryset = queryset.filter(client=c)
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super(ListCreateAPIView, self).create(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class SingleVisitView(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def put(self, request, *args, **kwargs):
        try:
            return super(RetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)
        except OperationalError as e:
            content = {'error': e.args[1]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# VisitTariff
class VisitTariffView(ListCreateAPIView):
    queryset = VisitTariff.objects.all()
    serializer_class = VisitTariffSerializer


class SingleVisitTariffView(RetrieveUpdateDestroyAPIView):
    queryset = VisitTariff.objects.all()
    serializer_class = VisitTariffSerializer

