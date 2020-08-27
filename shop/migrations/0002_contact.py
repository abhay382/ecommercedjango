# Generated by Django 2.1.5 on 2020-08-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(default='', max_length=700)),
                ('phone', models.CharField(default='', max_length=700)),
                ('desc', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
