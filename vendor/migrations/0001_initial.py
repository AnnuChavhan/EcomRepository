# Generated by Django 2.2.3 on 2019-11-30 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('remarks', models.IntegerField()),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
            ],
        ),
    ]
