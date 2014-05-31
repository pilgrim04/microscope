__author__ = 'pilgrim'
# -*- coding: utf-8 -*-
SUIT_CONFIG = {
    'MENU': (
        'sites',
        {'app': 'account', 'models': ('user', 'city', 'diffusers',
                                      {"label":u'Выгрузка пользователей', "url":"admin:user_report"}), 'label': u'Пользователи'},
        {'app': 'auth', 'models': ('user',), 'permissions':('only_for_super',),}
    )
}