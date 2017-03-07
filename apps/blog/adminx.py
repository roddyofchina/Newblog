#coding:utf8
import xadmin
from xadmin import views
from .models import NavigationMenu, Category,Article,Tag,Links


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "博客后台管理"
    site_footer = "博客后台管理"

class  NavigrationMenuAdmin(object):
    list_display = ['name', 'index', 'url']
    search_fields = ['name','index']

class CategoryAdmin(object):
    list_display = ['name','title','keywords','created_time','last_modified_time']
    search_fields = ['name','keywords']

class ArticleAdmin(object):
    list_display = ['title','click_count','status','date_publish','last_modified_time','category','tag']
    search_fields = ['title','status']

class TagAdmin(object):
    list_display = ['name','created_time','last_modified_time']

class LinksAdmin(object):
    list_display=['name','url','add_time']
    search_fields = ['name','url']

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(NavigationMenu, NavigrationMenuAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Links, LinksAdmin)


