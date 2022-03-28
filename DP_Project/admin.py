from django.contrib import admin

from DP_Project.models.knapsack import Knapsack

admin.site.site_header = '项目管理后台'
admin.site.site_title = '项目管理后台'
admin.site.index_title = '项目管理后台'

class KnapsackAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume', 'worth')

admin.site.register(Knapsack, KnapsackAdmin)
