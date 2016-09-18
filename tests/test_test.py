import pytest


def test_currency_widget_is_present(currency_widget):
    """
    Step 1:
        Open http://www.sberbank.ru/ru/person

    Step 2:
        Check that currency widget is displayed fine
    """
    with pytest.allure.step("Check that currency widget is displayed fine"):
        assert currency_widget.title == "Курсы"
        assert not currency_widget.widget_icons.is_displayed()
        assert currency_widget.body.is_displayed()


def test_currency_widget_icon_hider(currency_widget):
    """
    Step 1:
        Open http://www.sberbank.ru/ru/person

    Step 2:
        Click on icon hider of currency widget

    Step 3:
        Check that currency widget's icons are displayed

    Step 4:
        Click on icon hider of currency widget

    Step 5:
        Check that currency widget's icons aren't displayed
    """
    with pytest.allure.step("Click on icon hider of currency widget"):
        currency_widget.icon_hider.click()

    with pytest.allure.step(
            "Check that currency widget's icons are displayed"):
        assert currency_widget.widget_icons.is_displayed()

    with pytest.allure.step("Click on icon hider of currency widget"):
        currency_widget.icon_hider.click()

    with pytest.allure.step(
            "Check that currency widget's icons aren't displayed"):
        assert not currency_widget.widget_icons.is_displayed()


def test_currency_widget_minimize(currency_widget):
    """
    Step 1:
        Open http://www.sberbank.ru/ru/person

    Step 2:
        Click on minimize icon of currency widget

    Step 3:
        Check that currency widget's body isn't dispayed

    Step 4:
        Click on minimize icon of currency widget

    Step 5:
        Check that currency widget's body is dispayed
    """
    with pytest.allure.step("Click on minimize icon of currency widget"):
        currency_widget.icon_hider.click()
        currency_widget.minimize_icon.click()

    with pytest.allure.step(
            "Check that currency widget's body isn't dispayed"):
        assert not currency_widget.body.is_displayed()

    with pytest.allure.step("Click on minimize icon of currency widget"):
        currency_widget.minimize_icon.click()

    with pytest.allure.step(
            "Check that currency widget's body is dispayed"):
        assert currency_widget.body.is_displayed()


def test_currency_widget_view_navigation_to_next_page(driver, currency_widget,
                                                      navigation):
    """
    Step 1:
        Open http://www.sberbank.ru/ru/person

    Step 2:
        Select on appropriate view in currency widget

    Step 3:
        Click on appropriate part of currency manager view

    Step 4:
        Check redirection url
    """
    click_view = getattr(
        currency_widget, "click_{}".format(navigation["view"])
    )
    part_of_view = getattr(
        currency_widget.view, "{}".format(navigation["part_of_view"])
    )

    with pytest.allure.step("Select {} view in currency widget".format(
            navigation["view"])):
        click_view()

    with pytest.allure.step(
            "Click on {} of currency manager view".format(
                navigation["part_of_view"])):
        part_of_view.click()

    with pytest.allure.step("Check that redirection url is {}".format(
            navigation["target"])):
        assert navigation["target"] == driver.current_url

