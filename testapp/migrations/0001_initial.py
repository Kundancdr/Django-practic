# Generated by Django 5.0.2 on 2024-04-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_no', models.IntegerField()),
                ('e_name', models.CharField(max_length=30)),
                ('e_sal', models.FloatField()),
            ],
        ),
    ]
