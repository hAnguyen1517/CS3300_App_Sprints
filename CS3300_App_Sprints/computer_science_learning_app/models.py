from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Defines a Django model class named Usersys.
# This model inherits properties and behaviors from Django's models.Model,
# allows it to define fields and perform database operations.
# class Usersys(models.Model):
#     # An attribute representing Primary Key for the Usersys table
#     UserID = models.AutoField(primary_key=True)
#     # An attribute representing the username field in the Usersys table.
#     Username = models.CharField(max_length=100)
#     # An attribute representing the password field (assumed hashed) in the Usersys table.
#     Password = models.CharField(
#         max_length=100
#     )  # Assuming hashed password will be stored
#     #  An attribute representing the email field in the Usersys table.
#     Email = models.EmailField()
#     # A list of tuples defining the choices available for the role field in the Usersys table 
#     # Role choices field (e.g., student, parent, teacher)
#     Role_choices = [
#         ("student", "Student"),
#         ("parent", "Parent"),
#         ("teacher", "Teacher"),
#     ]
#     # An attribute representing the role field in the Usersys table. 
#     Role = models.CharField(max_length=20, choices=Role_choices)

#     # Defines a method to represent the object as a string
#     def __str__(self):
#         # Return the 'Username' attribute of the object as the string representation
#         return self.Username
#     # Define a method to get the absolute URL of the object
#     def get_absolute_url(self):
#         # Use the Django reverse function to generate the URL for the 'user-detail' view,
#         # passing the 'UserID' of the current object as an argument
#         return reverse("user-detail", args=[str(self.UserID)])

class UsersysManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='student'):
        """
        Creates and saves a User with the given username, email, password, and role.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, role='admin'):
        """
        Creates and saves a superuser with the given username, email, password, and role.
        """
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            role=role,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usersys(AbstractBaseUser):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(unique=True)
    Role_choices = [
        ("student", "Student"),
        ("parent", "Parent"),
        ("teacher", "Teacher"),
    ]
    Role = models.CharField(max_length=20, choices=Role_choices, default='student')
    
    objects = UsersysManager()

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.Username

    def get_full_name(self):
        return self.Username

    def get_short_name(self):
        return self.Username
    
# Defines a Django model class named Game.
# This model inherits properties and behaviors from Django's models.Model,
# allows it to define fields and perform database operations.
class Game(models.Model):
    # Primary Key for the Game table
    GameID = models.AutoField(primary_key=True)
    # Title field
    Title = models.CharField(max_length=100)
    # Description field
    Description = models.TextField()
    # Category field
    Category = models.CharField(max_length=50)
    # Difficulty Level field
    Difficulty_Level = models.CharField(max_length=20)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("game-detail", args=[str(self.GameID)])

# Defines a Django model class named LearningResource.
# This model inherits properties and behaviors from Django's models.Model,
# allows it to define fields and perform database operations.
class LearningResource(models.Model):
    # Primary Key for the LearningResource table
    ResourceID = models.AutoField(primary_key=True)
    # Title field
    Title = models.CharField(max_length=100)
    # Type choices field (e.g., lesson, tutorial, movie)
    Type_choices = [("lesson", "Lesson"), ("tutorial", "Tutorial"), ("movie", "Movie")]
    # Type field
    Type = models.CharField(max_length=20, choices=Type_choices)
    # Description field
    Description = models.TextField()
    # Content field (link to content or stored content)
    Content = models.CharField(max_length=200)
    # Age Appropriateness field
    Age_Appropriateness = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("learning-detail", args=[str(self.ResourceID)])

# Defines a Django model class named Progress.
# This model inherits properties and behaviors from Django's models.Model,
# allows it to define fields and perform database operations.
class Progress(models.Model):
    # Primary Key for the Progress table
    ProgressID = models.AutoField(primary_key=True)
    # UserID field (Foreign Key to User)
    UserID = models.ForeignKey(Usersys, on_delete=models.CASCADE)
    # ResourceID field (Foreign Key to LearningResource)
    ResourceID = models.ForeignKey(LearningResource, on_delete=models.CASCADE)
    # Completion Status field
    CompletionStatus = models.CharField(max_length=20)
    # Grade field
    Grade = models.FloatField()
    # Time Spent field
    TimeSpent = models.IntegerField()

    def __str__(self):
        return self.UserID

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.ProgressID)])

# Defines a Django model class named PerformanceReport.
# This model inherits properties and behaviors from Django's models.Model,
# allows it to define fields and perform database operations.
class PerformanceReport(models.Model):
    # Primary Key for the PerformanceReport table
    ReportID = models.AutoField(primary_key=True)
    # UserID field (Foreign Key to User)
    UserID = models.ForeignKey(Usersys, on_delete=models.CASCADE)
    # Tasks Completed field
    TasksCompleted = models.IntegerField()
    # Average Grade field
    AverageGrade = models.FloatField()
    # Areas For Development field
    AreasForDevelopment = models.TextField()

    def __str__(self):
        return self.UserID

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.ReportID)])
