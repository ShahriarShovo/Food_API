from django.contrib import admin
from authentication.models.user_token import UserToken
from authentication.models.user_profile import Profile
from authentication.models.user import User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(UserToken)
