# Generated by Django 4.1.3 on 2022-11-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
