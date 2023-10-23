from django.contrib import admin
from .models import *
# Register your models here.

class subcat(admin.ModelAdmin):
    list_display=['prod_name','prod_desc','M_R_P','prod_id']

class im(admin.ModelAdmin):
    list_display=['name']
# image
admin.site.register(crewNeckImg,im)
admin.site.register(DropCutImg,im)
admin.site.register(OversizedImg,im)
# CrewNeckMen 
admin.site.register(crewNeckMen,subcat)

# dropCut Men
admin.site.register(DropCutMen,subcat)

# Oversized Men
admin.site.register(OversizedMen,subcat)

# Men
admin.site.register(men)
# CrewNeckWomen
admin.site.register(crewNeckWomen,subcat)

# dropCut Women
admin.site.register(DropCutWomen,subcat)

# Oversized Women
admin.site.register(OversizedWomen,subcat)

# Women
admin.site.register(women)

admin.site.register(main)