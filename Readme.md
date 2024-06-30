# Yatra

Yatra is a tourism management web application built using Django REST framework (DRF). It enables users to explore and manage tourist destinations efficiently.

## Technologies Used

- **Backend Framework:** Django with Django REST framework
- **Database:** MySQL
- **Frontend:** HTML, CSS (Bootstrap for styling)
- **Deployment:** Local development server

## Features

- CRUD operations for tourist destinations: create, read, update, delete
- Detailed entries: place name, weather, location (state, district), Google Maps link, image, description
- Responsive and user-friendly interface

## Why Django REST framework (DRF)?

DRF is chosen for its:
- Powerful serialization
- Built-in authentication and authorization mechanisms
- Extensive documentation and community support
- Ability to create flexible and scalable APIs
- Seamless integration with Django's ORM for database operations

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your/repository.git
   cd yatra_project
2. **Install dependencies**
```sh
pip install -r requirements.txt
3. **Database configurations**
Ensure MySQL is installed and running.
Update database settings in settings.py to use MySQL.

4.**Run migrations**
```sh
python manage.py makemigrations
python manage.py migrate


5. **Start the development server:**

6. **Access the application:**
Open your web browser and go to `http://localhost:8000/`

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

