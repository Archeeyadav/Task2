# SearchEngine

![Search Data](https://github.com/Archeeyadav/SearchEngine/blob/main/home.png?raw=true)

## Requirements

- Python (version 3.9)
- Django (version 4.2.5)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Archeeyadav/SearchEngine.git
    cd SearchEngine
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Migrate the database:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Load Default Data

To populate your project's database with default data, you can use the following commands:

1. Access the Django shell:

    ```bash
    python manage.py shell
    ```

2. In the Python shell, run the following commands to load default data:

    ```python
    from user.dump_data import load_data
    load_data()
    ```

This will populate your database with default data if it's empty.
