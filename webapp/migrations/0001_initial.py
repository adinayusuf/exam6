# Generated by Django 4.0.5 on 2022-07-02 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('text', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Текст')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('edittime', models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=15, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
                'db_table': 'guestbook',
            },
        ),
    ]
