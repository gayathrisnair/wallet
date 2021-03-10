# Generated by Django 3.1 on 2021-03-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('minBalance', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'wallet',
            },
        ),
    ]
