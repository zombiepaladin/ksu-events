from django.apps import AppConfig
from django.conf import settings

class OAuth2Config(AppConfig):
    name = 'ksu_events.oauth2'

    def ready(self):
        # Override the default settings with package defaults if not provided by the consumer
        default_settings = {
            'SOCIALACCOUNT_PROVIDERS': SOCIALACCOUNT_PROVIDERS,
            'ACCOUNT_ADAPTER': 'ksu_events.oauth2.accountAdapter.CustomAccountAdapter',
            'SOCIALACCOUNT_ADAPTER': 'ksu_events.oauth2.provider.MLHProvider',
            # Add more defaults as needed
        }

        for setting, value in default_settings.items():
            if not hasattr(settings, setting):
                setattr(settings, setting, value)
