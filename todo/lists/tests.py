from django.test import TestCase
from django.http import  HttpRequest,HttpResponse
from .views import home_page
class HomePageTest(TestCase):
    def test_to_return_correct_html(self):
        #Django client

        request = HttpRequest()
        response = home_page(request)
        html_response = response.content.decode('utf8')
        self.assertTrue(html_response.startswith("<html>"))
        self.assertIn("<title>To-Do</title>", html_response)
        self.assertTrue(html_response.endswith("</html>"))


    #def test_are_we_using_correct_home_template(self):
    # what templates used?

    #def test_can_save_a_post_request(self):
    #def test_only_saves_items_when_necessary(self):
    #def test_redirects_after_POST(self):

#model class test for todo item