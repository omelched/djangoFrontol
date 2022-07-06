from django.apps import AppConfig


class FrontolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontol'
    external_actions: dict[str, callable] = {}

    def external_actions_parser(self, action: str) -> callable:
        return self.external_actions.get(action)


