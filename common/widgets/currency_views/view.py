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
