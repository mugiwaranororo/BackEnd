# Generated by Django 3.2.12 on 2023-02-18 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0008_auto_20230218_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunglasses',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sunglasses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
