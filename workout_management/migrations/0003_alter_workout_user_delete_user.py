# Generated by Django 4.2.11 on 2024-05-05 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout_management', '0002_remove_nutrition_user_remove_paymentdetail_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
