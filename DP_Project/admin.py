from django.contrib import admin

from DP_Project.models.knapsack import Knapsack
from DP_Project.models.logging import Logging

admin.site.site_header = '项目管理后台'
admin.site.site_title = '项目管理后台'
admin.site.index_title = '项目管理后台'


class KnapsackAdmin(admin.ModelAdmin):
    list_display = ('number', 'volume', 'worth')


class LoggingAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation', 'time')


admin.site.register(Knapsack, KnapsackAdmin)
admin.site.register(Logging, LoggingAdmin)
