from common.widgets.currency_views.view import View


class MetalView(View):

    def _create_tables(self):
        self.metal = {"body": {}}

        for row in self.body.find_elements_by_tag_name("tr"):
            cols = self._get_text(row.find_elements_by_tag_name("td"))

            assert len(cols) == 3

            self.metal["body"][cols[0]] = {"Buy": cols[1], "Sell": cols[2]}
