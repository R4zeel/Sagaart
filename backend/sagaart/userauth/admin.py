from django.contrib import admin

from userauth.models import User, UserSubscribe


class IngredientRecipeInline(admin.TabularInline):
    model = UserSubscribe
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline,)

    list_display = (
        "id",
        "email",
        "user_name",
        "telephone",
    )

    search_fields = (
        "id",
        "email",
        "user_name",
        "telephone",
    )

    empty_value_display = "Не задано"


class UserSubscribeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tariff",
        "cost",
        "status",
        "date_start",
        "date_end",
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserSubscribe, UserSubscribeAdmin)
