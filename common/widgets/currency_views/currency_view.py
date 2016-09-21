from common.widgets.currency_views.view import View


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
