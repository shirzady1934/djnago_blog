from django.contrib import admin
from .models import Post, Token, UserProfile, Comment, Notification
admin.site.register(Post)
admin.site.register(Token)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)