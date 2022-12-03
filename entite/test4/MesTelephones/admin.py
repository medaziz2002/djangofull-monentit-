from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from MesTelephones.models import Telephone, Type

class TelephonesAdmin(admin.ModelAdmin):
   list_display = ('nom', 'type_link', 'prix', 'realisateur')
   list_filter = ('nom', 'prix')
   date_hierarchy = 'datedecreation'
   ordering = ('datedecreation',)
   search_fields = ('nom', 'qte') 
   fields = ("type", "nom", "realisateur","prix","datedecreation")
   
   def type_link(self, typ):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:MesTelephones_type_change", args=(typ.type.pk,)),
            typ.type.nomType
        ))    

class TypeAdmin(admin.ModelAdmin):
   list_display = ('nomType', 'apercu')
   list_filter = ('nomType','id')
   search_fields = ('nom', 'realisateur') 
   def apercu (self, typ):
        text = typ.description[:40]
        if len(typ.description) > 40:
            return '{}...'.format(text)
        else:
            return typ.description

admin.site.register(Telephone, TelephonesAdmin)
admin.site.register(Type, TypeAdmin)

