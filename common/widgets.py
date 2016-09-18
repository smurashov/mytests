class Widget:
    def __init__(self, widget):
        self.widget = widget
        self.headers = self.widget.find_element_by_class_name(
            "personalized-widget-head"
        )
        self.title = self.headers.find_element_by_class_name(
            "personalized-widget-title"
        ).text
        self.widget_icons = self.headers.find_element_by_class_name(
            "widget-icons"
        )
        self.icon_hider = self.headers.find_element_by_class_name(
            "widget-icon-hider"
        )
        self.minimize_icon = self.widget_icons.find_element_by_class_name(
            "minimize-w"
        )
        self.remove_icon = self.widget_icons.find_element_by_class_name(
            "remove-w"
        )
        self.catalog_icon = self.widget_icons.find_element_by_class_name(
            "catalog-w"
        )
        self.body = self.widget.find_element_by_class_name("bp-widget-body")


class CurrencyWidget(Widget):

    class View:
        def __init__(self, body_section):
            self.header = body_section.find_element_by_tag_name("table")
            self.header_text = self._get_text(
                self.header.find_elements_by_tag_name("td")
            )
            self.body = body_section.find_element_by_class_name(
                "currency-body"
            )
            self._create_tables()

        def _create_tables(self):
            raise NotImplemented

        def _get_text(self, ll):
            return list(map(lambda x: x.text, ll))

    class CurrencyView(View):

        def __init__(self, body_section):
            super().__init__(body_section)
            self.help_icon = body_section.find_element_by_class_name(
                "sbr-tooltip-icon"
            )

        def _create_tables(self):
            self.remote_exchange_table = {}
            self.local_exchange_table = {}
            tables = [self.remote_exchange_table, self.local_exchange_table]
            table_headers = self._get_text(
                self.body.find_elements_by_tag_name("p")
            )
            table_bodies = self.body.find_elements_by_tag_name("table")

            assert len(table_headers) == 2 and len(table_bodies) == 2

            for table, header, body in zip(tables, table_headers,
                                           table_bodies):
                table["header"] = header
                table_body = body
                table["body"] = {}
                for row in table_body.find_elements_by_tag_name("tr"):
                    cols = self._get_text(row.find_elements_by_tag_name("td"))

                    assert len(cols) == 3

                    table["body"][cols[0]] = {"Buy": cols[1], "Sell": cols[2]}

    class MetalView(View):

        def _create_tables(self):
            self.metal = {"body": {}}

            for row in self.body.find_elements_by_tag_name("tr"):
                cols = self._get_text(row.find_elements_by_tag_name("td"))

                assert len(cols) == 3

                self.metal["body"][cols[0]] = {"Buy": cols[1], "Sell": cols[2]}

    def __init__(self, widget):
        super().__init__(widget)
        self.rates = self.body.find_element_by_class_name(
            "personal-rates"
        )
        self.tabs = self.rates.find_elements_by_tag_name("li")

        self._currencies = self.tabs[0]
        self._metals = self.tabs[1]
        self.current_body_content = "currency"
        self.view = CurrencyWidget.CurrencyView(
            self.rates.find_element_by_class_name(self.current_body_content)
        )

    def _get_view(self):
        if self.current_body_content == "currency":
            self.view = CurrencyWidget.CurrencyView(
                self.rates.find_element_by_class_name(
                    self.current_body_content
                )
            )
        elif self.current_body_content == "metal":
            self.view = CurrencyWidget.MetalView(
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
