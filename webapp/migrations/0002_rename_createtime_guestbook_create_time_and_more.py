# Generated by Django 4.0.5 on 2022-07-02 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestbook',
            old_name='createtime',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='guestbook',
            old_name='edittime',
            new_name='edit_time',
        ),
    ]
