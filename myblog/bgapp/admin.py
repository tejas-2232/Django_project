from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Userdata

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","Last_updated","timestamp"]
    list_display_links = ["Last_updated"] #if one clicks on timestamp- will redirect to post.
    list_filter = ["title","timestamp","Last_updated"]
    search_fields = ["title","content","Last_updated"]
    list_editable = ["title"] #edit the title of post
    class Meta:
        model=Post

class usermodeladmin(admin.ModelAdmin):
    list_display = ['username','userid','followers','following','Last_updated','timestamp']
    list_filter = ['userid','username']
    list_display_links = ['username']
    search_fields = ['username','userid','followers']
    list_editable = ['followers']

    class Meta:
        model=Userdata

admin.site.register(Userdata,usermodeladmin)
admin.site.register(Post,PostModelAdmin,) #register Post model into admin site
