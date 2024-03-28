from django.db import models
from django.urls import reverse 

class Usersys(models.Model):
    # Primary Key for the User table
    UserID = models.AutoField(primary_key=True)
    # Username field
    Username = models.CharField(max_length=100)
    # Password field (assumed hashed)
    Password = models.CharField(max_length=100)  # Assuming hashed password will be stored
    # Email field
    Email = models.EmailField()
    # Role choices field (e.g., student, parent, teacher)
    Role_choices = [
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('teacher', 'Teacher')
    ]
    # Role field
    Role = models.CharField(max_length=20, choices=Role_choices)

    def __str__(self):
        return self.Username
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.UserID)])


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
        return reverse('game-detail', args=[str(self.GameID)])

class LearningResource(models.Model):
    # Primary Key for the LearningResource table
    ResourceID = models.AutoField(primary_key=True)
    # Title field
    Title = models.CharField(max_length=100)
    # Type choices field (e.g., lesson, tutorial, movie)
    Type_choices = [
        ('lesson', 'Lesson'),
        ('tutorial', 'Tutorial'),
        ('movie', 'Movie')
    ]
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
        return reverse('learning-detail', args=[str(self.ResourceID)])
    
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
        return reverse('user-detail', args=[str(self.ProgressID)])

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
        return reverse('user-detail', args=[str(self.ReportID)])
