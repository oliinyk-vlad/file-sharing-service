# Generated by Django 3.0.8 on 2020-07-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FileField(upload_to='')),
                ('expires_at', models.DateTimeField(help_text='Format: 2020-07-25 00:00:00')),
            ],
        ),
    ]
