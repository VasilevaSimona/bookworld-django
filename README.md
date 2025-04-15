# bookworld-django

<h1>BookWorld Django Application</h1>

BookWorld is a Django-based web application that allows users to manage and display books, authors, and publications. It provides functionality for users to add books to their collection, view books as cards and in a table, and manage authors and publication details.

<h2>Features</h2>
<li>Book Management: Add books with titles, ISBN, content, and cover image.</li>

<li>Author Management: View and manage author details such as name and birth year.</li>

<li>Publication Management: Manage publication details including name, address, and related authors.</li>

<li>Interactive UI: Books are displayed as cards and in a tabular format.</li>

<li>Form-Based Interaction: Users can easily add books via an interactive form.</li>

<h2>Setup</h1>
<h3>Prerequisites<h2>
<li>Python 3.x</li>

<li>Django 3.x or later</li>

<li>Database (SQLite, PostgreSQL, etc.)</li>
<br>
<h2>Instalattion Steps
<ol>
<li>Clone the Repository</li>
git clone https://github.com/VasilevaSimona/bookworld-django.git
cd bookworld-django
<li>Install Dependencies</li>
pip install -r requirements.txt
<li>Apply Migrations</li>
python manage.py migrate
<li>Create a Superuser</li>
python manage.py createsuperuser
<li>Run the Server</li>
python manage.py runserver
<li>Access the application by navigating to http://127.0.0.1:8000/ in your web browser.</li>
<br>
<h2>Admin Panel</h2>
<ul>
<li>Navigate to the Django admin panel at http://127.0.0.1:8000/admin/.</li>
<li>Use the superuser credentials created above to log in and manage authors, books, and publications.</li>