# polling-app-django

The polling-app-django is a web application that allows users to create and participate in polls.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The polling-app-django is a web application that allows users to create and participate in polls. The application features user authentication, poll creation and voting functionality, as well as an admin interface for managing polls.

## Features

- User authentication
- Poll creation and voting functionality
- Admin interface for managing polls

## Technologies Used

- Django
- Django REST framework
- PostgreSQL
- React
- Bootstrap

## Installation

To run the polling-app-django locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/Bezyl-Mophat-Otieno/polling-app-django.git
```

2. Create a virtual environment:

```
cd polling-app-django
python -m venv env
```

3. Activate the virtual environment:

- On macOS and Linux:

```
source env/bin/activate
```

- On Windows:

```
env\Scripts\activate
```

4. Install the dependencies:

```
pip install -r requirements.txt
```

5. Create a PostgreSQL database and add the credentials to the `polls/settings.py` file:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<database_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. Run the migrations:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

8. In a new terminal, navigate to the client directory and install the dependencies:

```
cd client
npm install
```

9. Start the client:

```
npm start
```

10. Open your browser and go to `http://localhost:3000`.

## Usage

To use the polling-app-django, create an account and log in. You can then create polls, vote on polls, and view the results. If you are an admin, you can also manage polls through the admin interface.

## Contributing

Contributions to polling-app-django are always welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Implement your feature or bug fix.
4. Write tests if applicable.
5. Run tests and ensure they pass.
6. Commit your changes and push to your branch.
7. Create a pull request.

Please make sure to follow the code style and testing guidelines outlined in the repository.

## License

polling-app-django is licensed under the MIT License.
