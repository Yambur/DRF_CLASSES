from django.contrib import admin
from users.models import User,Payment

admin.site.register(User)

@admin.register(Payment)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date','course_paid','subject_paid','payment_amount','payment_method',)
    search_fields = ('user','course_paid','subject_paid','payment_method',)
