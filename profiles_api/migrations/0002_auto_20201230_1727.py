# Generated by Django 3.1.4 on 2020-12-30 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles_api.address'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles_api.city'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles_api.country'),
        ),
    ]
