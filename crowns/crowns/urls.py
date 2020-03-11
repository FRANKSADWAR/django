

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    
]

admin.site.site_header = "Crown Routes"
admin.site.site_title = "Crown PLC"
admin.site.index_title =  "Admin Apps"
