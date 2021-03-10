"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers
from walletApp import views
                    # add this
# from Crud import views                                # add this
        
# router = routers.DefaultRouter()                      # add this
# router.register(r'posts', views.PostView, 'Crud')     # add this
        


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/wallet/phoneNumber/<int:phoneNumber>/balance', views.get_balance),
    path('api/wallet', views.add_wallet),
    path('api/wallet/phoneNumber/<int:phoneNumber>/credit', views.add_credit),
    path('api/wallet/phoneNumber/<int:phoneNumber>/debit', views.debit_wallet),


    # path('api/', include(router.urls))
]
