from django.contrib import admin
from .models import Influencer, Content, DailyStats


class InfluencerAdmin(admin.ModelAdmin):
    """Here we make make DateFields visible in Admin panel"""
    readonly_fields = ("date_created", "date_updated",)


class ContentAdmin(admin.ModelAdmin):
    """Here we make make DateFields visible in Admin panel"""
    readonly_fields = ("date_created",)


class DailyStatsAdmin(admin.ModelAdmin):
    """Here we make make DateFields visible in Admin panel"""
    readonly_fields = ("date_of_update", )


# Register your models here.
admin.site.register(Influencer, InfluencerAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(DailyStats, DailyStatsAdmin)
# ToDo: create columns in admin panel to display - (date/channel_name/video_name)