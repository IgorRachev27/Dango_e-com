from django.contrib import admin
from .models import Order
# Register your models here.




class OrderAdm(admin.ModelAdmin):
    list_display = ('id','user', 'product','quantity','phone','date')
    list_display_links = ('id','product')
    search_fields = ('id','user', 'product','date')
    list_filter = ('date',) # запятая обязательна чтобы пайтон увидел строку как кортеж
    list_editable = ('quantity', 'phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id','user', 'product','quantity','phone','date')
    readonly_fields = ('date', 'id', 'user', 'product')
    # поле класса coment
    # inlines = [Comment,]


admin.site.register(Order,OrderAdm)