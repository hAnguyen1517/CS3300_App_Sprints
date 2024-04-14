from django.test import TestCase
from computer_science_learning_app.forms import LoginForm, SignupForm, GameForm, UsersysForm, LearningResourceForm, ProgressForm, PerformanceReportForm

# Testing for the User Login form
class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

# Testing for the User Signup form
class SignupFormTest(TestCase):
    def test_signup_form_valid(self):
        form_data = {'Username': 'testuser', 'Email': 'test@example.com', 'password': 'testpassword', 'Role': 'student'}
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form_data = {'Username': '', 'Email': 'test@example.com', 'password': 'testpassword', 'Role': 'student'}
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

# Testing for the Game creation form
class GameFormTest(TestCase):
    def test_game_form_valid(self):
        form_data = {'Title': 'Test Game', 'Description': 'Test Description', 'Category': 'Test Category', 'Difficulty_Level': 'Easy'}
        form = GameForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_game_form_invalid(self):
        form_data = {'Title': '', 'Description': 'Test Description', 'Category': 'Test Category', 'Difficulty_Level': 'Easy'}
        form = GameForm(data=form_data)
        self.assertFalse(form.is_valid())