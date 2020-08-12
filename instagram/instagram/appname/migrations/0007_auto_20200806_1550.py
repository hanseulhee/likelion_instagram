# Generated by Django 3.0.8 on 2020-08-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0006_auto_20200805_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='place',
            field=models.CharField(max_length=100),
        ),
    ]
