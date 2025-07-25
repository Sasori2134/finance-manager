# Generated by Django 5.2.2 on 2025-06-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_budget_user_id_alter_recurringbills_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringbills',
            name='date',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recurringbills',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
