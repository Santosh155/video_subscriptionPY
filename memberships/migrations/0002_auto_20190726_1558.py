# Generated by Django 2.2.3 on 2019-07-26 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermembership',
            old_name='stripe_customers_id',
            new_name='stripe_customer_id',
        ),
    ]
