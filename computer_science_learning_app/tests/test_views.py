from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from computer_science_learning_app.models import Usersys, Game, LearningResource, Progress, PerformanceReport
from computer_science_learning_app.forms import SignupForm, LoginForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_index_view(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_view_POST(self):
        response = self.client.post(self.register_url, {
            'Username': 'testuser',
            'Email': 'test@example.com',
            'password': 'testpassword',
            'Role': 'student'
        })

        self.assertEquals(response.status_code, 302)

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_view_POST(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        user.save()

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEquals(response.status_code, 200)

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/logout/')
