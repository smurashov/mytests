from common.widgets.widget import Widget
from common.widgets.currency_views.currency_view import CurrencyView
from common.widgets.currency_views.metal_view import MetalView


class CurrencyWidget(Widget):

    def __init__(self, widget):
        super().__init__(widget)
        self.rates = self.body.find_element_by_class_name(
            "personal-rates"
        )
        self.tabs = self.rates.find_elements_by_tag_name("li")

        self._currencies = self.tabs[0]
        self._metals = self.tabs[1]
        self.current_body_content = "currency"
        self.view = CurrencyView(
            self.rates.find_element_by_class_name(self.current_body_content)
        )

    def _get_view(self):
        if self.current_body_content == "currency":
            self.view = CurrencyView(
                self.rates.find_element_by_class_name(
                    self.current_body_content
                )
            )
        elif self.current_body_content == "metal":
            self.view = MetalView(
                self.rates.find_element_by_class_name(
                    self.current_body_content
                )
            )
        else:
            raise AttributeError("Unknown content {}".format(
                self.current_body_content
            ))

    def click_metals(self):
        self._metals.click()
        self.current_body_content = "metal"
        self._get_view()

    def click_currency(self):
        self._currencies.click()
        self.current_body_content = "currency"
        self._get_view()
