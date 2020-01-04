
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'swagger/', schema_view),
    path('admin/', admin.site.urls),
    url('api/v1/',include('customer.urls')),#
    url(r'^api/v1/', include('rest_framework.urls')),
    #url('accounts/',include('account.urls')),
    #url('address/',include('address.urls')),
    #url('products/',include('product.urls')),
    #url('vendors/',include('vendor.urls')),
]
