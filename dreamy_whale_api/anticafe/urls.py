from django.urls import path

from .views import *


app_name = "anticafe"

urlpatterns = [
    # AccountingEntry
    path('accounting_entries/', AccountingEntryView.as_view()),
    path('accounting_entries/<int:pk>', SingleAccountingEntryView.as_view()),
    # AccountingEntryType
    path('accounting_entry_types/', AccountingEntryTypeView.as_view()),
    path('accounting_entry_types/<int:pk>', SingleAccountingEntryTypeView.as_view()),
    # Calculator
    path('calculator/', CalculatorView.as_view()),
    # Card
    path('cards/', CardView.as_view()),
    path('cards/<int:pk>', SingleCardView.as_view()),
    # CardStatus
    path('card_statuses/', CardStatusView.as_view()),
    path('card_statuses/<int:pk>', SingleCardStatusView.as_view()),
    # CardType
    path('card_types/', CardTypeView.as_view()),
    path('card_types/<int:pk>', SingleCardTypeView.as_view()),
    # Client
    path('clients/', ClientView.as_view()),
    path('clients/<int:pk>', SingleClientView.as_view()),
    # ClientCard
    path('client_cards/', ClientCardView.as_view()),
    path('client_cards/<int:pk>', SingleClientCardView.as_view()),
    # ClientSubscription
    path('client_subscriptions/', ClientSubscriptionView.as_view()),
    path('client_subscriptions/<int:pk>', SingleClientSubscriptionView.as_view()),
    # Cost
    path('costs/', CostView.as_view()),
    path('costs/<int:pk>', SingleCostView.as_view()),
    # CostType
    path('cost_types/', CostTypeView.as_view()),
    path('cost_types/<int:pk>', SingleCostTypeView.as_view()),
    # Questionnaire
    path('form/', QuestionnaireView.as_view()),
    path('form/<int:pk>', SingleQuestionnaireView.as_view()),
    # ReferralSystem
    path('referral_system/', ReferralSystemView.as_view()),
    path('referral_system/<int:pk>', SingleReferralSystemView.as_view()),
    # ReservationObject
    path('reservation_objects/', ReservationObjectView.as_view()),
    path('reservation_objects/<int:pk>', SingleReservationObjectView.as_view()),
    # Reservation
    path('reservations/', ReservationView.as_view()),
    path('reservations/<int:pk>', SingleReservationView.as_view()),
    # ReservationTariff
    path('reservation_tariff/', ReservationTariffView.as_view()),
    path('reservation_tariff/<int:pk>', SingleReservationTariffView.as_view()),
    # Scan
    path('scanner/', ScanView.as_view()),
    path('scanner/<int:pk>', SingleScanView.as_view()),
    # Subscription
    path('subscriptions/', SubscriptionView.as_view()),
    path('subscriptions/<int:pk>', SingleSubscriptionView.as_view()),
    # Visit
    path('visits/', VisitView.as_view()),
    path('visits/<int:pk>', SingleVisitView.as_view()),
    # VisitTariff
    path('visit_tariff/', VisitTariffView.as_view()),
    path('visit_tariff/<int:pk>', SingleVisitTariffView.as_view()),
]
