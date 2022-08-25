from django.db import models

# Create your models here.
class HomeBG(models.Model):
    img = models.ImageField('HomeBG image', upload_to='media')

class TUser(models.Model):
    img = models.ImageField('TUser image', upload_to='media')
    name = models.CharField('TUser name', max_length = 30)
    about = models.CharField('TUser about', max_length = 30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'TUser'
        verbose_name_plural = 'TUsers'