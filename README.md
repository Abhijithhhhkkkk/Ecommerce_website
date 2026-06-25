# EASIB

A fashion e-commerce website built with Django and Tailwind CSS. This project was developed for learning full-stack web development concepts including product management, cloud media storage, content management, and Django Admin customization.

---

## Features

* Dynamic homepage banner management
* Product listing by category
* Product detail pages
* Product image gallery
* Order management through Django Admin
* Responsive UI with Tailwind CSS
* AWS S3 integration for media storage
* Admin-controlled content management
* Media upload and management

---

## Tech Stack

* Python
* Django
* HTML5
* Tailwind CSS
* SQLite
* AWS S3

---

## Project Structure

```text
Ecommerce_website/
│
├── Ecommerce_web/
├── blog/
├── templates/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Abhijithhhhkkkk/Ecommerce_website.git
cd Ecommerce_website
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/Ecommerce_admin/
```

---

## AWS S3 Integration

The project uses Amazon S3 for storing and serving product images and other media files. This provides scalable and reliable cloud-based storage instead of relying on local media storage.

---

## Learning Objectives

This project was built to gain practical experience in:

* Django Models
* Django Admin Customization
* URL Routing
* Template Rendering
* CRUD Operations
* Static and Media File Handling
* AWS S3 Integration
* E-Commerce Application Development

---

## Future Improvements

* User Registration and Authentication
* Shopping Cart Functionality
* Wishlist System
* Product Search and Filtering
* Order Tracking
* Payment Gateway Integration
* REST API Development

---

## Screenshots

### Homepage

<p align="center">
  <img src="screenshots/Screenshot From 2026-06-25 12-53-20.png" width="900">
</p>

### Product Detail Page

<p align="center">
  <img src="screenshots/Screenshot From 2026-06-25 12-52-37.png" width="900">
</p>

### Django Admin Dashboard

<p align="center">
  <img src="screenshots/Screenshot From 2026-06-25 12-45-51.png" width="900">
</p>

## Author

**Abhijith K**

