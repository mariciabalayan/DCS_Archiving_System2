from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import Faculty, Contact, Alternate_email

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
'''
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
class UserAdmin(admin.ModelAdmin):
        list_display = ('username', 'password', 'is_staff', 'is_active', 'is_superuser')

'''
class UserProfileInline(admin.StackedInline):
        #model=Faculty
        can_delete = False

class ContactInline(admin.StackedInline):
        model=Contact
        extra=1

class Alternate_emailInline(admin.StackedInline):
        model = Alternate_email
        extra = 1

class UserProfileAdmin(UserAdmin):
        list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
        #fieldsets = [
        #        ('Login credentials',           {'fields': ['username','password','is_staff', 'is_active', 'is_superuser']}),
        #        ('Date information',            {'fields': ['last_login', 'date_joined']}),
        #        ('Personal information',        {'fields': ['email','first_name', 'last_name']}),
        #]
        inlines=[ContactInline, Alternate_emailInline,]


admin.site.unregister(User)
del User.get_absolute_url
admin.site.register(User, UserProfileAdmin)
