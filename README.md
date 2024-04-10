**CS3300_App_Sprints:**  https://github.com/hAnguyen1517/CS3300_App_Sprints 

**GitHub Sprint01 Project Board:** https://github.com/users/hAnguyen1517/projects/4/views/1

**UML class diagram for model:** https://bit.ly/UMLClassDiagram 

# Computer Science Learning Application

Welcome to our Computer Science Learning Application! This application is designed to provide an interactive and engaging platform for users to enhance their knowledge and skills in various computer science topics. Whether you're a student, parent, or teacher, there's something here for everyone.

#  Tables and Functionalities
# Users
UserID: Unique identifier for each user (Primary Key)

Username: User's login username

Password: Securely hashed password for authentication

Email: User's email address for communication

Role: Role of the user (e.g., student, parent, teacher)

# Games
GameID: Unique identifier for each game (Primary Key)

Title: Title of the game

Description: Brief description of the game

Category: Category or genre of the game

Difficulty Level: Difficulty level of the game

# LearningResource
ResourceID: Unique identifier for each learning resource (Primary Key)

Title: Title of the resource

Type: Type of resource (e.g., lesson, tutorial, movie)

Description: Description of the resource

Content: Link to the resource content or stored content

Age Appropriateness: Age appropriateness of the resource

# Progress
ProgressID: Unique identifier for each progress record (Primary Key)

UserID: Reference to the user (Foreign Key to User)

ResourceID: Reference to the learning resource (Foreign Key to LearningResource)

CompletionStatus: Status of completion for the resource

Grade: Grade achieved for the resource

TimeSpent: Time spent by the user on the resource

# Performance Report
ReportID: Unique identifier for each performance report (Primary Key)

UserID: Reference to the user (Foreign Key to User)

TasksCompleted: Number of tasks completed by the user

AverageGrade: Average grade achieved by the user

AreasForDevelopment: Areas identified for the user's development

# Learning Reference
PreferenceID: Unique identifier for each learning preference (Primary Key)

UserID: Reference to the user (Foreign Key to User)

SubjectPreference: User's preference for subjects

DifficultyLevelPreference: User's preference for difficulty levels

# Feedback
FeedbackID: Unique identifier for each feedback (Primary Key)

UserID: Reference to the user (Foreign Key to User)

TaskID: Reference to the task (Foreign Key to Task)

FeedbackMessage: Message providing feedback

Correctness: Indicates correctness of the feedback

# Collaboration
CollaborationID: Unique identifier for each collaboration (Primary Key)

UserID: Reference to the user (Foreign Key to User)

ProjectID: Reference to the project (Foreign Key to Project)

Contribution: User's contribution to the project

# How to Use
Registration: Users can register with their username, email, and password. They need to specify their role (student, parent, or teacher) during registration.
Authentication: Once registered, users can log in using their username and password.
Exploring Games: Users can explore various educational games categorized based on difficulty level and category.

Accessing Learning Resources: Users can access learning resources such as lessons, tutorials, and movies categorized by subject and age appropriateness.
Tracking Progress: Users can track their progress by monitoring completion status, grades, and time spent on each resource.

Performance Reports: Users can view performance reports detailing tasks completed, average grades, and areas for development.
Setting Preferences: Users can set their learning preferences regarding subjects and difficulty levels.

Providing Feedback: Users can provide feedback on resources, tasks, and correctness.
Collaboration: Users can collaborate on projects by contributing their skills and knowledge.

# Get Involved
We're constantly striving to improve our platform. If you have any suggestions, feedback, or would like to contribute, feel free to reach out to us!

Thank you for choosing our Computer Science Learning Application. Let's embark on a journey of knowledge together! 🚀

