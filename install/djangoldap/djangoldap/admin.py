from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from djangoldap.models import gvOrganisation

@admin.register(gvOrganisation)
class gvOrganisationAdmin(admin.ModelAdmin):
    exclude = ['dn']
    list_display = ['gvOuId', 'cn']
    search_fields = ['gvOuId', 'cn', 'o']
