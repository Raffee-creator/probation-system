# Generated by Django 4.2.9 on 2024-03-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsApp', '0004_visitors_case_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='comment',
            field=models.TextField(default='No ccomment', max_length=200),
        ),
    ]
