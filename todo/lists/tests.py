from django.test import TestCase
from django.http import  HttpRequest,HttpResponse
from .views import home_page
from .models import TodoItem
class HomePageTest(TestCase):
    # def test_to_return_correct_html(self):
    #     #Django client
    #     response = self.client.post('/todo/', data = {'item_text':'my new todo item'})
    #     # request = HttpRequest()
    #     # response = home_page(request)
    #     print(response.content.decode('utf8'))
    #     html_response = response.content.decode('utf8')
    #     self.assertTrue(response.startswith("<html>"))
    #     self.assertIn("<title>To-Do</title>", response)
    #     self.assertTrue(response.endswith("</html>"))

    # def test_are_we_using_correct_home_template(self):
    #     response = self.client.post('/todo/', data={'item_text': 'my new todo item'})
    #
    #     self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/todo/', data={'item_text': 'my new todo item2'})
        print(response)
        self.assertEqual(TodoItem.objects.count(),1)
        self.assertEqual('my new todo item2',TodoItem.objects.first().text)
        #self.assertIn('my new todo item2', response.content.decode())

    def test_redirects_after_POST(self):
        response = self.client.post('/todo/', data={'item_text': 'my new todo item2'})
        print(response.content.decode())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'],'/todo/')

#model class test for todo item
class TodoItemTest(TestCase):
    def test_saving_objects_in_database(self):
        first_item = TodoItem()
        first_item.text = 'my item1'
        first_item.save()
        second_item = TodoItem()
        second_item.text = 'my item2'
        second_item.save()
        all_items = TodoItem.objects.all()
        self.assertEqual(2,TodoItem.objects.count())

        first_item = all_items[0]
        second_item = all_items[1]

        self.assertEqual('my item1', first_item.text)
        self.assertEqual('my item2', second_item.text)