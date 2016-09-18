import allure
import xml.etree.ElementTree as ET
import os
import pytest
from selenium import webdriver

from common.pages import PersonPage

path = os.path.join(os.path.dirname(__file__), "testdata.xml")
tree = ET.parse(path)
root = tree.getroot()
browsers = []
for browser in root.findall('browser'):
    browsers.append(browser.attrib["name"])

navigation_attrs = list(map(lambda x: x.attrib, root.findall('navigation')))

print(browsers, navigation_attrs)


@pytest.fixture(scope='module', params=browsers)
def driver(request):
    d = getattr(webdriver, request.param)()
    request.addfinalizer(lambda: d.close())
    return d


@pytest.fixture(scope='function')
def currency_widget(request, driver):
    with pytest.allure.step("Open http://www.sberbank.ru/ru/person"):
        page = PersonPage(driver)
    widget = page.get_currency_widget()
    request.addfinalizer(lambda: page.get_page())
    return widget


@pytest.fixture(scope='function', params=navigation_attrs)
def navigation(request):
    return request.param


