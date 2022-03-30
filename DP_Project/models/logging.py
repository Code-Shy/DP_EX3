from django.db import models


class Logging(models.Model):
    operation = models.CharField(max_length=256, verbose_name="操作")
    time = models.DateTimeField(max_length=19, verbose_name="时间")

    class Meta:
        verbose_name = "日志记录"
        verbose_name_plural = "日志记录"
        ordering = ('id', )

    def __str__(self):
        return str(self.id)
