# Generated by Django 4.1.5 on 2023-06-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='user/')),
            ],
            options={
                'db_table': 'user_tb',
            },
        ),
    ]
