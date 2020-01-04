from django.contrib import admin
from django.urls import path
from customer.views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customers', CustomerOp)
urlpatterns = router.urls

'''

import sys
sys.exit(0)
urlpatterns = [
    path('welcome', welcome_customer_page),
    path('persist/', save_or_update),
    path("delete/<int:cid>",delete_customer),
    path("edit/<int:cid>",fetch_customer)
]
'''