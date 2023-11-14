from django.db import models


class Post(models.Model):
    '''даннные поста'''
    title = models.CharField('заголовок поста', max_length=100)
    description = models.TextField('текст поста')
    author = models.CharField('имя автора', max_length=100)
    date = models.DateField('дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

