# Generated by Django 4.2.9 on 2024-03-07 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmsApp', '0007_remove_visitors_comments_alter_visitors_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitors',
            old_name='comment',
            new_name='comments',
        ),
    ]
