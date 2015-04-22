from django.contrib import admin

# Register your models here.
from .models import Question, Choice
# Choice objects are edited on the Question admin page. 
# By default, provide enough fields for 3 choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # display individual fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # filter
    list_filter = ['pub_date']
    # search box
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)