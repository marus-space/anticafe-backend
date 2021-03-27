from django.contrib import admin

from .models import AccountingEntry, AccountingEntryType, Card, CardStatus, \
    CardType, Client, ClientCard, ClientSubscription, Cost, CostType, Event, \
    Log, Subscription, Visit, VisitTariff

admin.site.register(AccountingEntry)
admin.site.register(AccountingEntryType)
admin.site.register(Card)
admin.site.register(CardStatus)
admin.site.register(CardType)
admin.site.register(Client)
admin.site.register(ClientCard)
admin.site.register(ClientSubscription)
admin.site.register(Cost)
admin.site.register(CostType)
admin.site.register(Event)
admin.site.register(Log)
admin.site.register(Subscription)
admin.site.register(Visit)
admin.site.register(VisitTariff)
