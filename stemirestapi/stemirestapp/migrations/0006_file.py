# Generated by Django 2.2.5 on 2019-09-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stemirestapp', '0005_auto_20190911_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'File',
            },
        ),
    ]
