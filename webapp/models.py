from django.db import models

STATUS = [('active', 'Активно'), ('blocked', 'Заблокировано')]


# Create your models here.

class GuestBook(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя")
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Текст")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField( max_length=15, choices=STATUS, null=False, default=STATUS[0][0], verbose_name='Статус')

    def __str__(self):
        return f'{self.id}.{self.name}: {self.status} '

    class Meta:
        db_table = 'guestbook'
        verbose_name = 'Текст'
        verbose_name_plural = 'Текста'
