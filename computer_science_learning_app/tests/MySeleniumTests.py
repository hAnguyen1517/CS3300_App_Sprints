import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from computer_science_learning_app.models import (
    Usersys,
    Game,
    LearningResource,
    Progress,
    PerformanceReport,
)

# class initiating the selenium tests
class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(20)
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    # Test 1 to check login and userlist page when successful login
    def test_login_and_access_usersys_list(self):
        # Open the login page
        self.selenium.get(self.live_server_url + reverse("login_page"))

        # Log in with test user credentials
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("hanh")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("hanh")
        password_input.submit()

        # Verify that we are redirected to the index page after login
        self.assertIn("Login", self.selenium.title)

        # Now, navigate to the Home page
        self.selenium.get(self.live_server_url + reverse("index"))

        # Check that we are on the Usersys list page
        self.assertIn("Homepage", self.selenium.title)

        # Open the registration page
        self.selenium.get(self.live_server_url + reverse("register_page"))

        # Fill in the registration form
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("new_user")
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys("new_user@example.com")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("new_password")

        # Verify that we are redirected to the login page after registration
        self.assertIn("Login", self.selenium.title)

        # Now try to login with the newly registered user
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("new_user")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("new_password")
        password_input.submit()

        # Verify that we are redirected to the index page after login
        self.assertIn("Login", self.selenium.title)

    # Test 2 to create games and check if we are able to retrieve the game inserted
    def test_game_details_view(self):
        # Create a game object
        game = Game.objects.create(
            Title="Test Game",
            Description="Test Description",
            Category="Test",
            Difficulty_Level="Easy",
        )

        # Navigate to the game details page
        self.selenium.get(
            self.live_server_url + reverse("game_detail", args=[game.pk])
        )

        # Check that the game details are displayed correctly
        self.assertIn("Test Game", self.selenium.title)
        self.assertIn("Test Description", self.selenium.page_source)
        self.assertIn("Test", self.selenium.page_source)
        self.assertIn("Easy", self.selenium.page_source)

    # Test 3 to create learning resources and check if we are able to retrieve the learning resource inserted
    def test_learning_resource_access(self):
        # Create a learning resource object
        resource = LearningResource.objects.create(
            Title="Test Resource",
            Type="lesson",
            Description="Test Description",
            Content="http://example.com",
            Age_Appropriateness="All Ages",
        )

        # Navigate to the learning resource page
        self.selenium.get(
            self.live_server_url + reverse("learning_resource_detail", args=[resource.pk])
        )

        # Check that the learning resource details are displayed correctly
        self.assertIn("Test Resource", self.selenium.title)
        self.assertIn("Test Description", self.selenium.page_source)
        self.assertIn("All Ages", self.selenium.page_source)
        self.assertIn("http://example.com", self.selenium.page_source)

    # Test 4 to create user object and learning resource and check if we are able to retrieve them
    def test_progress_tracking(self):
        # Create a user object
        user = Usersys.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            role="teacher",
            password="test_password",
        )

        # Create a learning resource object
        resource = LearningResource.objects.create(
            Title="Test Resource",
            Type="lesson",
            Description="Test Description",
            Content="http://example.com",
            Age_Appropriateness="All Ages",
        )

        # Navigate to the learning resource page
        self.selenium.get(
            self.live_server_url + reverse("learning_resource_detail", args=[resource.pk])
        )

     
        # Check that progress is correctly tracked for the user
        progress = Progress.objects.filter(UserID=user, ResourceID=resource).first()
        self.assertIsNotNone(progress)
        self.assertEqual(progress.CompletionStatus, "Completed")
     

if __name__ == "__main__":
    unittest.main()
