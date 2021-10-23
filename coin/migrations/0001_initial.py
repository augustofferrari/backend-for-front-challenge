# Generated by Django 3.2.8 on 2021-10-23 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('abbreviation', models.CharField(max_length=50, unique=True)),
                ('current_price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('low_price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('high_price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('volume', models.DecimalField(decimal_places=4, max_digits=12)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CoinReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.PositiveIntegerField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='coin.coin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='coinreview',
            constraint=models.UniqueConstraint(fields=('user', 'coin'), name='unique user and coin review'),
        ),
        migrations.AddConstraint(
            model_name='coinreview',
            constraint=models.CheckConstraint(check=models.Q(('ranking__range', (1, 5))), name='check ranking value'),
        ),
    ]
