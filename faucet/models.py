import datetime

from .configs import local_settings as configs
from django.db import models

NETWORK_VK, NETWORK_FACEBOOK, NETWORK_GOOGLE, NETWORK_TWITTER = 'vk', 'facebook', 'google', 'twitter'

class Account(models.Model):
    NETWORKS = [
        (NETWORK_VK, 'VK'),
        (NETWORK_FACEBOOK, 'Facebook'),
        (NETWORK_GOOGLE, 'Google'),
        (NETWORK_TWITTER, 'Twitter'),
    ]

    name = models.CharField('Аккаунт', max_length=255, unique=True)
    ip = models.CharField('IP', max_length=100, unique=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    authorized_network = models.CharField('Соц. сеть', choices=NETWORKS, max_length=12)
    uid = models.CharField('UID', max_length=100)
    first_name = models.CharField('Имя', max_length=150,)
    last_name = models.CharField('Фамилия', max_length=150)
    photo = models.URLField('Фотография', max_length=255)

    @staticmethod
    def get_ips():
        allowedAge = datetime.datetime.now() - datetime.timedelta(seconds=configs.MIN_IP_AGE)
        return list(Account.objects.filter(created__gt=allowedAge).values_list('ip', flat=True))

    @staticmethod
    def exists(ip):
        return ip in Account.get_ips()

    def __str__(self):
        return 'Аккаунт: %s' % self.name

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
        unique_together = ('authorized_network', 'uid')


class Lecture(models.Model):
    NETWORKS = [
        (NETWORK_VK, 'VK'),
        (NETWORK_FACEBOOK, 'Facebook'),
        (NETWORK_GOOGLE, 'Google'),
        (NETWORK_TWITTER, 'Twitter'),
    ]

    type = models.CharField('Соц. сеть', choices=NETWORKS, max_length=12)
    url = models.URLField('Ссылка в социальной сети', max_length=255)
    account_name = models.CharField('Аккаунт', max_length=150)

    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name = 'лекция'
        verbose_name_plural = 'лекции'
        unique_together = ('type', 'url')
