from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp # it's like from newsletter.models import SignUp' but since we are inside newsletter, it's n necessary

# Let's customize how the admin works
class SignUpAdmin(admin.ModelAdmin):
	# Define what I want to see on the page
    list_display = ["__str__", "full_name", "organization", "timestamp", "updated"]
    form = SignUpForm
    #class Meta:
    #    model = SignUp

admin.site.register(SignUp, SignUpAdmin)
