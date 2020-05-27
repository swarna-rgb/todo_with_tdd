from django.test import TestCase
from django.http import  HttpRequest,HttpResponse
from .views import home_page
from .models import TodoItem,User
import unittest
class HomePageTest(TestCase):
    def test_home_page_uses_home_html(self):
        response = self.client.get('/todo/')
        self.assertTemplateUsed(response,'home.html')
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

    # def test_can_save_a_post_request(self):
    #     response = self.client.post('/todo/', data={'item_text': 'my new todo item2'})
    #     print(response)
    #     self.assertEqual(TodoItem.objects.count(),1)
    #     self.assertEqual('my new todo item2',TodoItem.objects.first().text)
    #     #self.assertIn('my new todo item2', response.content.decode())

    # def test_redirects_after_POST(self):
    #     response = self.client.post('/todo/', data={'item_text': 'my new todo item2'})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['Location'],'/todo/showall/')

class ShowAllTodoItems(TestCase):
    def test_showall_todo_items(self):
        response = self.client.get('/todo/showall/')
        self.assertTemplateUsed(response,'list.html')

    def test_saving_and_retrieving_data_using_user_and_todo_object(self):
        # auser = User()
        # auser.save()
        auser = User.objects.create()
        first_item = TodoItem.objects.create(text='myitem1', user=auser)
        second_item = TodoItem.objects.create(text='myitem2', user=auser)
        response = self.client.get(f'/todo/{auser.id}/')
        self.assertContains(response,'myitem1')
        self.assertContains(response, 'myitem2')

        buser = User.objects.create()
        first_item = TodoItem.objects.create(text='myitem3', user=buser)
        second_item = TodoItem.objects.create(text='myitem4', user=buser)
        response = self.client.get(f'/todo/{buser.id}/')
        self.assertNotContains(response, 'myitem1')
        self.assertNotContains(response, 'myitem2')
        self.assertContains(response, 'myitem3')
        self.assertContains(response, 'myitem4')


        # # first_item = TodoItem()
        # # first_item.text = 'myitem1'
        # # first_item.user = user
        # # first_item.save()
        # # second_item = TodoItem()
        # # second_item.text = 'myitem1'
        # second_item.user = user


    @unittest.skip
    def test_display_all_items(self):
        #response = self.client.post('/todo/newtodoitem/', data={'item_text':'myitem1'})
          TodoItem.objects.create(text='myitem2')
        # TodoItem.objects.create(text='myitem2')
          response = self.client.get('/todo/showall/')
          self.assertContains(response,'myitem2' )
        # self.assertContains(response, 'myitem2')

    def test_show_todo_items_for_that_user_only(self):
        user = User.objects.create()
        TodoItem.objects.create(text='Test unique url for a user', user=user)
        print(f'/todo/{user.id}/')
        response = self.client.get(f'/todo/{user.id}/')
        print('*test_show_todo_items_for_that_user_only*')
        print(response)
        self.assertContains(response,'Test unique url for a user')

        #print(f'/todo/{todo_obj.id}/')
        # response = self.client.get(f'/todo/{todo_obj.id}/')
        # print(response)
        # self.assertContains(response,'Test unique url for a user')


class NewTodoItem(TestCase):
    def test_can_save_a_request_to_an_existing_user(self):
        auser = User.objects.create()
        buser = User.objects.create()
        self.client.post(f'/todo/{auser.id}/additem/',
                         data={'item_text':'Adding item to the existing list'})
        self.assertEqual(1, TodoItem.objects.count())
        self.assertEqual('Adding item to the existing list', TodoItem.objects.first().text)
        self.assertEqual(TodoItem.objects.first().user,auser)

    def test_existing_user_redirect_after_post(self):
        auser = User.objects.create()
        response = self.client.post(f'/todo/{auser.id}/additem/',
                         data={'item_text': 'Adding item to the existing list'})
        self.assertRedirects(response, f'/todo/{auser.id}/' )

    def test_redirects_after_POST(self):
        response = self.client.post('/todo/newtodoitem/', data={'item_text': 'my new todo item2'})
        print(response)
       # self.assertRedirects(response, f'/todo/{}')

        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['Location'],'/todo/showall/')

    def test_save_post_data(self):
        response = self.client.post('/todo/newtodoitem/', data={'item_text':'my new todo item'})
        print('***')
        print(response)
        self.assertEqual(TodoItem.objects.count(),1)

@unittest.skip
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