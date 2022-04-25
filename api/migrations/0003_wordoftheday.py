# Generated by Django 3.2.12 on 2022-04-25 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordOfTheDay',
            fields=[
                ('vocabulary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.vocabulary')),
            ],
            bases=('api.vocabulary',),
        ),
    ]