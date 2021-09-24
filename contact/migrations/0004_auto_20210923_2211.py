# Generated by Django 3.2.7 on 2021-09-23 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='emails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='contact.email'),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
