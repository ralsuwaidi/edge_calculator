from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CalculatorConfig(AppConfig):
    name = "edge_calculator.calculator"
    verbose_name = _("Calculators")

    def ready(self):
        try:
            import edge_calculator.users.signals  # noqa F401
        except ImportError:
            pass
