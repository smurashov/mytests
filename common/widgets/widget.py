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
