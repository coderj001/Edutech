from django.contrib import admin
from core.models import Question

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag_list', 'created_by', 'created_at']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
