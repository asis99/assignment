# Student Portal - Django Assignment

## Overview

This is a Django-based assignment project scaffold. Your task is to implement a basic **Student Portal** with class-based views, templates, and models.

You will define your own models based on the specifications below and use them to build views and templates for student dashboard, course listing, profile view, and a contact form.

---

## folder structure
student_portal/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       └── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── student_dashboard/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md


## 🔧 Model Design Specification

Define the following models in your Django app based on these requirements:

### 1. Student

Represents a student user in the system.

| Field Name       | Field Type       | Notes                          |
|------------------|------------------|--------------------------------|
| `name`           | `CharField`      | Max length: 100                |
| `email`          | `EmailField`     | Must be unique                 |
| `enrollment_date`| `DateField`      | Date the student enrolled      |

---

### 2. Course

Represents a course that can be enrolled in.

| Field Name       | Field Type       | Notes                          |
|------------------|------------------|--------------------------------|
| `title`          | `CharField`      | Max length: 100                |
| `description`    | `TextField`      | Course overview                |
| `credits`        | `IntegerField`   | Number of course credits       |

---

### 3. Enrollment

Links students to the courses they are enrolled in.

| Field Name       | Field Type       | Notes                          |
|------------------|------------------|--------------------------------|
| `student`        | `ForeignKey`     | Related to `Student`, `on_delete=models.CASCADE` |
| `course`         | `ForeignKey`     | Related to `Course`, `on_delete=models.CASCADE`  |
| `date_enrolled`  | `DateField`      | Date when enrollment occurred  |

---

### 4. ContactMessage

Stores messages submitted via a contact form.

| Field Name       | Field Type       | Notes                          |
|------------------|------------------|--------------------------------|
| `name`           | `CharField`      | Max length: 100                |
| `email`          | `EmailField`     | Email of the sender            |
| `message`        | `TextField`      | The message content            |
| `created_at`     | `DateTimeField`  | Auto-generated timestamp (`auto_now_add=True`) |

---

## 🎯 Assignment Tasks

You are required to implement the following features using **class-based views**:

1. **Dashboard View**
   - Displays basic stats (e.g., total students, total courses).
   - Uses `TemplateView`.

2. **Course Listing View**
   - List all available courses with title, description, and credits.
   - Uses `ListView` or `TemplateView`.

3. **Profile View**
   - Show details of a specific student (e.g., name, email, courses).
   - Uses `DetailView` or `TemplateView`.

4. **Contact Form View**
   - Submit a form to store contact messages.
   - Uses `FormView`.

---

## 🛠️ Technologies

- Python 3.x
- Django 4.x or higher
- SQLite (default DB)
- HTML/CSS (basic)

---

## 🚀 Getting Started

```bash
# Step 1: Migrate database
python manage.py makemigrations
python manage.py migrate

# Step 2: Run development server
python manage.py runserver
