# Generated by Django 2.1.1 on 2018-09-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListofItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=264, unique=True)),
                ('note', models.CharField(max_length=265, unique=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
