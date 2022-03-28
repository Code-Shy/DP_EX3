from django.db import models

class Knapsack(models.Model):
    worth = models.IntegerField(default=0.0, verbose_name="价值")
    volume = models.IntegerField(default=0.0, verbose_name="体积")

    class Meta:
        verbose_name = '背包数据'
        verbose_name_plural = '背包数据'
        ordering = ('id',)

    def __str__(self):
        return self.id
