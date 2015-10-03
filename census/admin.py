from django.contrib import admin

from .models import APISetting, HousingVariable, CensusInfo


class HousingVariableInline(admin.TabularInline):
    model = HousingVariable
    extra = 2


class APISettingAdmin(admin.ModelAdmin):
    list_display = ('api_description',)
    inlines = [HousingVariableInline]
    # exclude = ('api_used',)


admin.site.register(APISetting, APISettingAdmin)
admin.site.register(CensusInfo)
