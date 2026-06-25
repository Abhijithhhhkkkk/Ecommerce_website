A simple fashion e-commerce website built with Django for learning and portfolio purposes. The project demonstrates product management, dynamic content rendering, image handling, and Django Admin customization.

Features
Product listing page
Product detail page
Product image gallery
Dynamic homepage banner
Category-wise product display
Django Admin Panel
Order management
User authentication (Admin)
Content management through admin dashboard

Tech Stack
Python
Django
HTML
Tailwind CSS
SQLite

Project Structure
EASIB/
│
├── ecommerce_web/
├── blog/
├── db.sqlite3
└── manage.py

Installation
Clone Repository
git clone https://github.com/Abhijithhhhkkkk/Ecommerce_website.git
cd Ecommerce_website
python -m venv venv
source venv/bin/activate
Run Migrations
python manage.py migrate

Start Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
Admin Panel

Create a superuser:
python manage.py createsuperuser
Admin URL:

http://127.0.0.1:8000/Ecommerce_admin/
Learning Objectives

This project was developed primarily for:

Understanding Django Models
Django Admin Customization
Template Rendering
Media File Handling
URL Routing
CRUD Operations
Basic E-Commerce Workflow
Future Improvements
Shopping Cart
User Registration & Login
Payment Gateway Integration
Search & Filtering
Wishlist
Order Tracking
REST API Integration
