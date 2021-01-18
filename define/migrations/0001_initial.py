# Generated by Django 3.1.5 on 2021-01-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Define',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('pegi', models.CharField(max_length=2)),
                ('commentCount', models.FloatField()),
                ('commentScore', models.FloatField()),
                ('appSizeMb', models.FloatField()),
                ('downloads', models.CharField(max_length=15)),
                ('ranking', models.CharField(max_length=7)),
            ],
        ),
    ]