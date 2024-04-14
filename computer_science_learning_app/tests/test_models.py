from django.test import TestCase
from computer_science_learning_app.models import Usersys, Game, LearningResource, Progress, PerformanceReport


class UsersysModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Usersys.objects.create(Username='testuser', Email='test@example.com', Role='student')

    def test_username_label(self):
        user = Usersys.objects.get(UserID=1)
        field_label = user._meta.get_field('Username').verbose_name
        self.assertEqual(field_label, 'Username')

    def test_get_full_name(self):
        user = Usersys.objects.get(UserID=1)
        self.assertEqual(user.get_full_name(), user.Username)


class GameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Game.objects.create(Title='Test Game', Description='Test Description', Category='Test Category', Difficulty_Level='Easy')

    def test_title_label(self):
        game = Game.objects.get(GameID=1)
        field_label = game._meta.get_field('Title').verbose_name
        self.assertEqual(field_label, 'Title')
class LearningResourceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        LearningResource.objects.create(Title='Test Resource', Type='lesson', Description='Test Description', Content='Test Content', Age_Appropriateness='Test Age')

    def test_title_label(self):
        resource = LearningResource.objects.get(ResourceID=1)
        field_label = resource._meta.get_field('Title').verbose_name
        self.assertEqual(field_label, 'Title')


class ProgressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = Usersys.objects.create(Username='testuser', Email='test@example.com', Role='student')
        resource = LearningResource.objects.create(Title='Test Resource', Type='lesson', Description='Test Description', Content='Test Content', Age_Appropriateness='Test Age')
        Progress.objects.create(UserID=user, ResourceID=resource, CompletionStatus='completed', Grade=100.0, TimeSpent=60)

    def test_completion_status_label(self):
        progress = Progress.objects.get(ProgressID=1)
        field_label = progress._meta.get_field('CompletionStatus').verbose_name
        self.assertEqual(field_label, 'Completion Status')


class PerformanceReportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = Usersys.objects.create(Username='testuser', Email='test@example.com', Role='student')
        PerformanceReport.objects.create(UserID=user, TasksCompleted=5, AverageGrade=90.0, AreasForDevelopment='Test areas')

    def test_tasks_completed_label(self):
        report = PerformanceReport.objects.get(ReportID=1)
        field_label = report._meta.get_field('TasksCompleted').verbose_name
        self.assertEqual(field_label, 'Tasks Completed')