# Generated by Django 4.1.7 on 2023-04-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_userdata_wallet_bit_alter_user_email_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='login_field',
            field=models.CharField(default=None, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
