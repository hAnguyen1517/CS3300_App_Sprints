import unittest
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from computer_science_learning_app.models import Usersys, Game, LearningResource, Progress, PerformanceReport
# from selenium.webdriver.chrome.webdriver import WebDriver

# Class method for the selenium tests
class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  
        cls.selenium.implicitly_wait(30)  
        cls.selenium.maximize_window()  

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_and_access_usersys_list(self):
    # Open the login page
        self.selenium.get(self.live_server_url + reverse('login_page'))

        # Log in with test user credentials
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test1')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('test')
        password_input.submit()

        # Verify that we are redirected to the index page after login
        self.assertIn('Welcome', self.selenium.title)

        # Now, navigate to the Usersys list page
        self.selenium.get(self.live_server_url + reverse('usersys_list'))

        # Check that we are on the Usersys list page
        self.assertIn('Users List', self.selenium.title)
       
       

if __name__ == '__main__':
    unittest.main()
