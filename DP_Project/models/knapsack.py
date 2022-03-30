from django.db import models


class Knapsack(models.Model):
    number = models.CharField(default=None, max_length=256, verbose_name="背包编号")
    volume = models.IntegerField(default=0.0, verbose_name="体积")
    worth = models.IntegerField(default=0.0, verbose_name="价值")

    class Meta:
        verbose_name = '背包数据'
        verbose_name_plural = '背包数据'
        ordering = ('number',)

    def __str__(self):
        return str(self.id)
