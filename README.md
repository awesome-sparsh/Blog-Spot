Developed by Sparsh Sethi
    https://www.sparshsethi.com
    https://github.com/awesome-sparsh/
    APP can be found at https://blog-spot-gfya.onrender.com

📝 Blog-Spot
Blog-Spot is a full-featured blogging platform built with Django. It allows users to create, edit, and manage blog posts with a clean and responsive interface.

🚀 Features
Create and read blog posts

Responsive design using HTML, CSS, and JavaScript

PostgreSQL database for development

🛠️ Installation
  Clone the repository:
    git clone https://github.com/awesome-sparsh/Blog-Spot.git
    cd Blog-Spot
  
  Create and activate a virtual environment:
    python -m venv venv
      # On Windows
        venv\Scripts\activate
      # On Unix or MacOS
        source venv/bin/activate
  
  Install dependencies:
    pip install -r requirements.txt
  
  Apply migrations:
    python manage.py migrate
  
  Create a superuser (optional, for admin access):
    python manage.py createsuperuser
  
  Run the development server:
    python manage.py runserver

📁 Project Structure
  Blog-Spot/
  ├── BlogApp/              # Main Django application
  │   ├── migrations/       # Database migrations
  │   ├── templates/        # HTML templates
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── db.sqlite3            # SQLite database
  ├── manage.py             # Django's command-line utility
  ├── requirements.txt      # Python dependencies
  └── README.md             # Project documentation

