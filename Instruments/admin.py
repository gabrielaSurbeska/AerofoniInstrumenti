from django.contrib import admin

from Instruments.models import Prodavac, Kupuvac, Slobodni_Aerofoni, Duvacki_Instrumenti, Register


# Register your models here.
class ProdavacAdmin(admin.ModelAdmin):
    list_display = ("Name", "Surname",)


    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True


    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False


    def has_view_permission(self, request, obj=None):
       return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False


admin.site.register(Prodavac, ProdavacAdmin)


class KupuvacAdmin(admin.ModelAdmin):
    list_display = ("Name", "Surname",)

    def has_add_permission(self, request, obj=None):
         return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Kupuvac, KupuvacAdmin)

class Slobodni_AerofoniAdmin(admin.ModelAdmin):
    list_display = ("Brand", "Model",)

    def has_add_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

admin.site.register(Slobodni_Aerofoni, Slobodni_AerofoniAdmin)


class Duvacki_InstrumentiAdmin(admin.ModelAdmin):
    list_display = ("Name", "Trumpets_Type",)

    def has_add_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False


admin.site.register(Duvacki_Instrumenti, Duvacki_InstrumentiAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ("Name", "Surname",)

    def has_add_permission(self, request, obj=None):
        return True


    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False


admin.site.register(Register, RegisterAdmin)

