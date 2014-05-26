from django.contrib import admin

from customer.models import Customer, Meeting

class MeetingInline(admin.TabularInline):
    model = Meeting
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","surname", "birth_date", "email", "country", "city", "address", "home_phone", "mobile_phone")
    model = Customer
    inlines = [MeetingInline,]


class MeetingAdmin(admin.ModelAdmin):
    list_display = ("meeting_type", "meeting_date", "meeting_project", "meeting_comment", "id")
    list_display_links = (["meeting_type"])
    model = Meeting


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Meeting,MeetingAdmin)