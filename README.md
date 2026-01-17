# Django Scaffold

A minimal Django project scaffold using Poetry for dependency management.

## Project Structure

```
django_escafoldo/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
├── README.md
└── config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Installation

### Prerequisites

- Python 3.10+
- Poetry

### Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd django_escafoldo
```

2. **Install dependencies**

```bash
poetry install
```

3. **Activate the virtual environment**

```bash
poetry shell
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

## Configuration

- **Settings**: Configuration is managed in `config/settings.py`
- **Dependencies**: Add packages using `poetry add <package-name>`
- **Environment Variables**: Use `.env` file for local configuration (add to `.gitignore`)

## Development

```bash
# Create new app
python manage.py startapp <app-name>

# Create migrations
python manage.py makemigrations

# Access Django shell
python manage.py shell
```
