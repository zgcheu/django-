
from django.contrib import admin
from django.urls import path,include

# 静态文件服务
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('sales/', include('sales.urls')),

    path('api/mgr/', include('mgr.urls'))
] +  static("/", document_root="./z_dist")

