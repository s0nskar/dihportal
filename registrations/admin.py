from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

# Some hack for changing default __unicode__ method for auth User model
# For displaying pretty dropdown of OneToOneToField
def get_name(self):
	return self.get_full_name()

User.__unicode__ = get_name

# UserProfileAdmin
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('get_name', 'get_email', 'contact', 'department')
	search_fields = ('user__email', 'id')
	list_filter = ('department',)
	fields = ['user', 'roll_no', 'contact', 'year','department']

	# __ doesn't work here
	def get_name(self, obj):
		return obj.user.get_full_name()
	get_name.admin_order_field = 'name'
	get_name.short_description = 'Full name'

	def get_email(self, obj):
		return obj.user.email
	get_email.admin_order_field = 'email'
	get_email.short_description = 'E-mail'

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Proposal)
