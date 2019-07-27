from django.contrib import admin

# Register your models here.

from .models import Membership, Subscription, UserMembership


admin.site.register(Membership)


admin.site.register(Subscription)


admin.site.register(UserMembership)