from django.db import models


class AccountingEntry(models.Model):
    accounting_entry_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    accounting_entry_type = models.ForeignKey('AccountingEntryType', models.DO_NOTHING)
    date = models.DateTimeField()
    cost_rub = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cost_min = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_entry'
        verbose_name = 'Проводка'
        verbose_name_plural = 'Проводки'

    def __str__(self):
        return '[%.16s] %s - %s - %s руб. %s мин' % (self.date, self.client, self.accounting_entry_type, self.cost_rub, self.cost_min)


class AccountingEntryType(models.Model):
    accounting_entry_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'accounting_entry_type'
        verbose_name = 'Тип проводки'
        verbose_name_plural = 'Типы проводок'

    def __str__(self):
        return self.name


class Card(models.Model):
    card_id = models.PositiveIntegerField(primary_key=True)
    card_type = models.ForeignKey('CardType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'card'
        verbose_name = 'Клубная карта'
        verbose_name_plural = 'Клубные карты'

    def __str__(self):
        return '%s - %s' % (self.card_id, self.card_type)


class CardStatus(models.Model):
    card_status_id = models.AutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'card_status'
        verbose_name = 'Статус клубной карты'
        verbose_name_plural = 'Статусы клубной карты'

    def __str__(self):
        return self.status


class CardType(models.Model):
    card_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'card_type'
        verbose_name = 'Тип клубной карты'
        verbose_name_plural = 'Типы клубной карты'

    def __str__(self):
        return self.name


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45, blank=True, null=True)
    phone = models.DecimalField(unique=True, max_digits=11, decimal_places=0)
    email = models.CharField(unique=True, max_length=80)
    date_of_birth = models.DateField()
    balance_rub = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    balance_min = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    payment_min_status = models.IntegerField(default=0)
    ban_status = models.IntegerField(default=0)
    ref_link_from = models.CharField(max_length=8, blank=True, null=True)
    ref_link = models.CharField(unique=True, max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return '[%s] %s %s' % (self.client_id, self.last_name, self.first_name)


class ClientCard(models.Model):
    client_card_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    card = models.ForeignKey(Card, models.DO_NOTHING)
    card_status = models.ForeignKey(CardStatus, models.DO_NOTHING)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_card'
        verbose_name = 'Клубная карта клиента'
        verbose_name_plural = 'Клубные карты клиентов'

    def __str__(self):
        return '[%.16s] %s - ID %s карта (%s)' % (self.date, self.client, self.card, self.card_status)


class ClientSubscription(models.Model):
    client_subscription_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    subscription = models.ForeignKey('Subscription', models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_subscription'
        verbose_name = 'Абонемент клиента'
        verbose_name_plural = 'Абонементы клиентов'

    def __str__(self):
        return '[%.16s - %.16s] Клиент %s - %s' % (self.start, self.end, self.client, self.subscription)


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
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return '[%.16s] %s - %s - %s руб. %s мин' % (self.date, self.client, self.cost_type, self.cost_rub, self.cost_min)


class CostType(models.Model):
    cost_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'cost_type'
        verbose_name = 'Тип расхода'
        verbose_name_plural = 'Типы расходов'

    def __str__(self):
        return self.name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'event'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


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
        verbose_name = 'Лог событий'
        verbose_name_plural = 'Логи событий'

    def __str__(self):
        return '[%.16s] %s' % (self.date, self.comment)


class ReferralSystem(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING, primary_key=True)
    num_of_invitees = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'referral_system'
        verbose_name = 'Реферальная система'

    def __str__(self):
        return '%s пригласил(а) %s друзей' % (self.client, self.num_of_invitees)


class Scan(models.Model):
    scan_id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Card, models.DO_NOTHING)
    scanner_type = models.CharField(max_length=20)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scan'
        verbose_name = 'Запись со сканера'
        verbose_name_plural = 'Записи со сканера'

    def __str__(self):
        return '[%.16s] %s ID %s' % (self.date, self.scanner_type, self.card)


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
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'

    def __str__(self):
        if self.start is None and self.end is None:
            interval = ''
        else:
            interval = 'с %.5s по %.5s - ' % (self.start, self.end)
        return '%s (%s%s ч) - %s руб.' % (self.name, interval, self.duration, self.cost_rub)


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
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return '[%.16s - %.16s] %s - %s' % (self.start, self.end, self.client, self.duration)


class VisitTariff(models.Model):
    visit_tariff_id = models.AutoField(primary_key=True)
    card_type = models.ForeignKey(CardType, models.DO_NOTHING, blank=True, null=True)
    start_tariff_zone = models.TimeField()
    end_tariff_zone = models.TimeField()
    cost_per_minute = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'visit_tariff'
        verbose_name = 'Тариф для посещений'
        verbose_name_plural = 'Тарифы для посещений'

    def __str__(self):
        if self.card_type is None:
            card_type = 'Клубные карты'
        else:
            card_type = str(self.card_type) + ' карта'
        return '%s - %.5s - %.5s - %s руб./мин' % (card_type, self.start_tariff_zone, self.end_tariff_zone, self.cost_per_minute)


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
