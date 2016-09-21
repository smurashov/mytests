from common.widgets.currency_widget import CurrencyWidget


class PersonPage:
    def __init__(self, driver, wait=15):
        self.driver = driver
        self.driver.implicitly_wait(wait)
        self.get_page()

    def back(self):
        self.driver.back()
        return self.get_currency_widget()

    def get_page(self):
        self.driver.get("http://www.sberbank.ru/ru/person")

    def get_currency_widget(self):
        try:
            return CurrencyWidget(
                next(
                    filter(
                        lambda x: "Курсы" in x.text,
                        self.driver.find_elements_by_class_name(
                            "flip-container"
                        )
                    )
                )
            )
        except StopIteration:
            raise Exception("Can't find currency widget")
