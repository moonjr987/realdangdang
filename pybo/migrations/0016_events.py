# Generated by Django 4.1.7 on 2023-05-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0015_alter_expert_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
    ]
