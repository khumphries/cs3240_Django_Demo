from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Data information',{'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'was_published_recently', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)



# Register your models here.
