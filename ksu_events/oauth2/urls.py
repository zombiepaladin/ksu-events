from django.urls import path, include
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from provider import MLHProvider

urlpatterns = [
    path('', include('allauth.urls')),  # Include all default allauth URLs
    path('mlh/', include(default_urlpatterns(MLHProvider))),  # Custom MLH OAuth URLs
]