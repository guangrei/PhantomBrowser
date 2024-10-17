# -*- coding: utf-8 -*-
import unittest
from PhantomBrowser import AsyncBrowser


class BrowserTest(unittest.IsolatedAsyncioTestCase):

    async def test_browser(self) -> None:
        browser = AsyncBrowser()
        await browser.get("https://example.com")
        self.assertEqual(isinstance(browser.response, bytes), True)
        await browser.close()
