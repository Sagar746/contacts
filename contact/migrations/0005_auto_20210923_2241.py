# Generated by Django 3.2.7 on 2021-09-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20210923_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='emails',
        ),
        migrations.AddField(
            model_name='email',
            name='contacts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.contact'),
        ),
    ]
