from django.contrib import admin
from .models import Question, Post, Photo, Expert, Pet, Events,Tanalyze,ForumQuestion,ForumAnswer, PatientList

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]





admin.site.register(PatientList)

admin.site.register(ForumQuestion)

admin.site.register(Pet)

admin.site.register(Expert)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Post, PostAdmin)
# Register your models here.


admin.site.register(Tanalyze)