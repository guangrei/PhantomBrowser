# -*- coding: utf-8 -*-
import unittest
from PhantomBrowser import Browser


class BrowserTest(unittest.TestCase):
    def test_browser(self) -> None:
        browser = Browser()
        browser.get("https://example.com", render="png")
        self.assertEqual(isinstance(browser.response, bytes), True)
        browser.close()
