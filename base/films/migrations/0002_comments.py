# Generated by Django 4.2.5 on 2024-01-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(db_index=True, max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]