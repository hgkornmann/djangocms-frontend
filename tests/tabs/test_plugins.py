from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_frontend.contrib.tabs.cms_plugins import (
    TabItemPlugin, TabPlugin,
)

from ..fixtures import TestFixture


class TabsPluginTestCase(TestFixture, CMSTestCase):

    def test_tab_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=TabPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nav')

    def test_tab_item_plugin(self):
        parent = add_plugin(
            placeholder=self.placeholder,
            plugin_type=TabPlugin.__name__,
            language=self.language,
        )
        plugin = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=TabItemPlugin.__name__,
            language=self.language,
            config=dict(tab_title="tab title"),
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div class="tab-content">')
        self.assertContains(response, 'tab-pane')