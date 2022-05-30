from django.db import models

class ToDo(models.Model):
    """ Model of ToDo
    """
    ToDo = models.TextField(max_length=2000, unique=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'

    def __str__(self) -> str:
        return f'{self.ToDo}'
