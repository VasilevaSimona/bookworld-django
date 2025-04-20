# bookworld-django

<h1>BookWorld Django Application</h1>

BookWorld is a Django-based web application that allows users to manage and display books, authors, and publications. It provides functionality for users to add books to their collection, view books as cards and in a table, and manage authors and publication details.

<h2>Features</h2>
<li>Book Management: Add books with titles, ISBN, content, and cover image.</li>

<li>Author Management: View and manage author details such as name and birth year.</li>

<li>Publication Management: Manage publication details including name, address, and related authors.</li>

<li>Interactive UI: Books are displayed as cards and in a tabular format.</li>

<li>Form-Based Interaction: Users can easily add books via an interactive form.</li>

<h1>Setup</h1>
<h2>Prerequisites</h2>
  
<li>Python 3.x</li>

<li>Django 3.x or later</li>

<li>Database (SQLite, PostgreSQL, etc.)</li>

<br>
<h2>Instalattion Steps</h2>

<li>Clone the Repository</li>
git clone https://github.com/VasilevaSimona/bookworld-django.git
<br>
cd bookworld-django</p>
<li>Install Dependencies</li>
pip install -r requirements.txt
<li>Apply Migrations</li>
python manage.py migrate
<li>Create a Superuser</li>
python manage.py createsuperuser
<li>Run the Server</li>
python manage.py runserver
<li>Access the application by navigating to http://127.0.0.1:8000/books in your web browser.</li>

<br>
<h2>Admin Panel</h2>
<ul>
<li>Navigate to the Django admin panel at http://127.0.0.1:8000/admin/.</li>
<li>Use the superuser credentials created above to log in and manage authors, books, and publications.</li>
</ul>
<br>
<h2>Admin Customizations</h2>
<li>AuthorAdmin: Custom admin interface for the Author model with additional controls for adding, editing, and deleting.</li>

<li>BookAdmin: Displaying books by title and author in the admin.</li>

<li>PublicationAdmin: Inline editing of authors associated with each publication.</li>
<br>
<h2>Templates</h2>
<li>Index Page: Displays books as cards and in a table format. Users can also add books via a form.</li>

<li>Book Table: Displays a table listing books with ISBN, title, and content.</li>

<li>Book Form: A form for adding books, including title, ISBN, short content, and cover image.</li>
<br>
<h2>Styling</h2>
<li>The app uses Bootstrap 5 for styling and responsiveness.</li>

<li>Custom CSS styles have been added for elements like cards, tables, forms, and buttons to enhance the user experience.</li>
