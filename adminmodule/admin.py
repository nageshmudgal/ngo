from django.contrib import admin
from .models import State,Admins,City,Member,MemberPost,Org,Campaign,Donations

admin.site.register(State)
admin.site.register(Admins)
admin.site.register(City)
admin.site.register(Member)
admin.site.register(MemberPost)
admin.site.register(Org)
admin.site.register(Campaign)
admin.site.register(Donations)
