# Ecommerce_website

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)]()
[![Django](https://img.shields.io/badge/django-4.x-green.svg)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()

A beginner-friendly E-Commerce website built with Django to learn web application fundamentals: models, templates, forms, authentication, and basic order/cart flows.

## Demo

> Add a screenshot or GIF to show the main product listing or cart.
![Demo screenshot](assets/screenshot.png) <!-- create assets/screenshot.png or update path -->

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Environment variables](#environment-variables)
- [Run locally](#run-locally)
- [Run tests](#run-tests)
- [Docker (optional)](#docker-optional)
- [Project structure](#project-structure)
- [Future improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features

- User registration, login and authentication
- Product listing and product detail pages
- Shopping cart (add/remove items)
- Order creation and simple order flow
- Admin panel for product & user management

## Tech Stack

- Python 3.x
- Django 4.x
- SQLite (development); optionally PostgreSQL for production
- HTML, CSS, JavaScript

## Prerequisites

- Python 3.8+
- git
- (Optional) Docker & Docker Compose

## Quickstart

1. Clone the repository:
   ```bash
   git clone https://github.com/Abhijithhhhkkkk/Ecommerce_website.git
   cd Ecommerce_website
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy example env (create a `.env` in project root) and set secrets:
   ```
   cp .env.example .env
   ```
   See [Environment variables](#environment-variables) below for required keys.

5. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```
   Open http://127.0.0.1:8000/

## Environment variables

Create a `.env` file (or use environment variables) containing at least:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3   # or your postgres URL
```

If you use django-environ or dj-database-url, ensure the settings read DATABASE_URL.

## Run tests

If you have tests, run:
```bash
python manage.py test
```
(Consider adding tests for models, views, and forms to increase reliability.)

## Docker (optional)

Add a Dockerfile and docker-compose.yml to make local setup reproducible. Example workflow:

1. Build:
   ```bash
   docker-compose build
   ```
2. Run migrations and start:
   ```bash
   docker-compose up
   ```

## Project structure (high-level)

- ecommerce_website/ — Django project settings
- apps/ or shop/ — main app(s): products, cart, orders, users
- templates/ — HTML templates
- static/ — CSS / JS / images
- requirements.txt — Python dependencies

(Adjust and expand this section to match your repo layout.)

## Future improvements

- Payment gateway integration (Stripe / PayPal)
- Product reviews & ratings
- Search, filtering and pagination
- Improve UI/UX and mobile responsiveness
- Deploy to Heroku / Vercel / DigitalOcean
- Add unit and integration tests
- Use PostgreSQL in production and environment-specific settings

## Contributing

Thanks for wanting to contribute! A simple workflow:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes and push: `git push origin feature/your-feature`
4. Open a pull request describing your changes

Consider adding a CONTRIBUTING.md and CODE_OF_CONDUCT.md for clarity.

## License

This project is provided under the MIT License. See LICENSE file for details. If you haven't added a license yet, consider adding one (MIT or another license you prefer).

## Author

Abhijith K — https://github.com/Abhijithhhhkkkk

Acknowledgements: Learning project inspired by Django tutorials and community resources.
