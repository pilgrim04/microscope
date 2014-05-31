__author__ = 'pilgrim'
# coding: utf-8


NEW = 0
WAITING = 1
PAYED = 2
LOADED = 3
RETURNED = 4
NO_ANSWER = 5


ORDERS_STATUS_CHOICES = (
    (NEW, u'Новый'),
    (WAITING, u'Ожидает оплаты'),
    (PAYED, u'Оплачен'),
    (LOADED, u'Отгружен'),
    (RETURNED, u'Возврат'),
    (NO_ANSWER, u'Нет ответа')
)

CASH = 0
CASHLESS = 1

ORDERS_PAY_CHOICES = (
    (CASH, u'Наличные'),
    (CASHLESS, u'Безналичные')
)

EMS = 0
SELF_DELIVERY = 1
COURIER = 2

ORDERS_DELIVERY_CHOICES = (
    (EMS, u'EMS'),
    (SELF_DELIVERY, u'Самовывоз'),
    (COURIER, u'Курьер')
)
