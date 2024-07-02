from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='posts/', null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'