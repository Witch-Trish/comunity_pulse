# Comunity Pulse

**Comunity Pulse** is a Flask-based web application that provides a RESTful API for managing questions, categories, and statistics. It is designed to collect and serve structured data, making it suitable for feedback systems, surveys, or analytics tools.

## Features

- Modular REST API using Flask Blueprints
- Category and question management endpoints
- Database migration management via Alembic
- Environment-based configuration

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Witch-Trish/comunity_pulse.git
   cd comunity_pulse
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. **Start the application:**

   ```bash
   python run.py
   ```

## Requirements

All required Python packages are listed in `requirements.txt`.


