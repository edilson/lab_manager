# Generated by Django 2.2.7 on 2019-11-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registration',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
