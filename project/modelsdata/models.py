from django.db import models
from django.urls import reverse


class Predictionmodel(models.Model):
    slug = models.SlugField()  # Для создания своего URL адреса
    title = models.CharField(max_length=120)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    img = models.ImageField(default='default.png', upload_to='model_images', blank=True, verbose_name='Изображение',
                            null=True)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['title']


class Predictionrequest(models.Model):
    slug = models.SlugField()  # Для создания своего URL адреса
    title = models.CharField(max_length=120, verbose_name='Наименование')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    predictionmodel = models.ForeignKey(Predictionmodel, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    addres_http = models.CharField(max_length=250, verbose_name='http-адрес', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'slug': self.predictionmodel.slug, 'request_slug': self.slug})

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
        ordering = ['title']
