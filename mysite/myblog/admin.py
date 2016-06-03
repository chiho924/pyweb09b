from django.contrib import admin

from myblog.models import Category
from myblog.models import Post


class MembershipInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )


class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
