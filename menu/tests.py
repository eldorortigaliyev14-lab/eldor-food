from django.test import TestCase


class HomePageTests(TestCase):
    def test_homepage_shows_menu_categories_and_contact_sections(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["menu_items"]), 48)
        self.assertContains(response, "Taom turlari")
        self.assertContains(response, "href=\"#contact\"")
        self.assertContains(response, "Bog'lanish")
        self.assertContains(response, "48 TA TAOM")
