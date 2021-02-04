from django.db import models

class Addressbar(models.Model):
    slug = models.SlugField()  # Для создания своего URL адреса
    title = models.CharField(max_length=120, verbose_name='Наименование')
    addres = models.URLField(max_length=250, verbose_name='url')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['title']