from django.db import models


class AccountingEntry(models.Model):
    accounting_entry_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    accounting_entry_type = models.ForeignKey('AccountingEntryType', models.DO_NOTHING)
    date = models.DateTimeField()
    cost_rub = models.DecimalField(max_digits=8, decimal_places=2)
    cost_min = models.DecimalField(max_digits=6, decimal_places=0)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_entry'


class AccountingEntryType(models.Model):
    accounting_entry_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'accounting_entry_type'


class Card(models.Model):
    card_id = models.DecimalField(primary_key=True, max_digits=12, decimal_places=0)
    card_type = models.ForeignKey('CardType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'card'


class CardStatus(models.Model):
    card_status_id = models.AutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'card_status'


class CardType(models.Model):
    card_type_id = models.AutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'card_type'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45, blank=True, null=True)
    phone = models.DecimalField(unique=True, max_digits=11, decimal_places=0)
    email = models.CharField(unique=True, max_length=80)
    date_of_birth = models.DateField()
    balance_rub = models.DecimalField(max_digits=8, decimal_places=2)
    balance_min = models.DecimalField(max_digits=6, decimal_places=0)
    ref_link_from = models.CharField(max_length=8, blank=True, null=True)
    ref_link = models.CharField(max_length=8)
    num_of_invitees = models.IntegerField()
    payment_min_status = models.IntegerField()
    ban_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client'


class ClientCard(models.Model):
    client = models.OneToOneField(Client, models.DO_NOTHING, primary_key=True)
    card = models.ForeignKey(Card, models.DO_NOTHING)
    card_status = models.ForeignKey(CardStatus, models.DO_NOTHING)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_card'
        unique_together = (('client', 'card'),)


class ClientSubscription(models.Model):
    client_subscription_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    subscription = models.ForeignKey('Subscription', models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_subscription'


class Cost(models.Model):
    cost_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    cost_type = models.ForeignKey('CostType', models.DO_NOTHING)
    date = models.DateTimeField()
    cost_rub = models.DecimalField(max_digits=8, decimal_places=2)
    cost_min = models.DecimalField(max_digits=6, decimal_places=0)
    bonus = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'cost'


class CostType(models.Model):
    cost_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'cost_type'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'event'


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    staff_account = models.CharField(max_length=45)
    comment = models.TextField(blank=True, null=True)
    client_id = models.PositiveIntegerField(blank=True, null=True)
    card_id = models.PositiveIntegerField(blank=True, null=True)
    visit_id = models.PositiveIntegerField(blank=True, null=True)
    client_subscription_id = models.PositiveIntegerField(blank=True, null=True)
    cost_id = models.PositiveIntegerField(blank=True, null=True)
    accounting_entry_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    duration = models.PositiveIntegerField()
    cost_rub = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'subscription'


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit'


class VisitTariff(models.Model):
    visit_tariff_id = models.AutoField(primary_key=True)
    card_type = models.ForeignKey(CardType, models.DO_NOTHING, blank=True, null=True)
    start_tariff_zone = models.TimeField()
    end_tariff_zone = models.TimeField()
    cost_per_minute = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'visit_tariff'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
