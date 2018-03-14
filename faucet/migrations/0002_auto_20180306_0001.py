# Generated by Django 2.0.2 on 2018-03-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'аккаунт', 'verbose_name_plural': 'аккаунты'},
        ),
        migrations.AddField(
            model_name='account',
            name='uid',
            field=models.CharField(default='', max_length=100, verbose_name='UID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='authorized_network',
            field=models.CharField(choices=[('vk', 'VK'), ('facebook', 'Facebook'), ('google', 'Google'), ('twitter', 'Twitter')], max_length=12, verbose_name='Соц. сеть'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=models.URLField(max_length=255, verbose_name='Фотография'),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('name', 'authorized_network', 'uid')},
        ),
    ]
