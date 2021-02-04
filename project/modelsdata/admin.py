from django.contrib import admin
from .models import Predictionmodel, Predictionrequest
from django.utils.html import format_html

class PredictionmodelInline(admin.TabularInline):
    model = Predictionmodel

    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width if obj.image.width < 200 else 200,
            height=obj.image.height if obj.image.height < 200 else 200,
        )
        )

    fields = ('title', 'img', 'get_preview', 'free', 'slug',)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PredictionmodelInline,
    ]

    fields = ('slug', 'title', 'number', 'addres_url',)

    class Meta:
        model = Predictionrequest


admin.site.register(Predictionmodel)
admin.site.register(Predictionrequest)


