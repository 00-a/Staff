from django.db import models


class Employee(models.Model):
    """Employee. Parent - employee chief"""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)
    salary = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',
                               verbose_name='Chief')
    photo = models.ImageField(upload_to='staffphotos/', blank=True)
    employment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Position(models.Model):
    """Employee position"""
    name = models.CharField(max_length=100, verbose_name='Position name')

    def __str__(self):
        return self.name
