# Direct Booking RESTful Web-Service
A simple direct booking API with commit booking and list bookings for a specific user services.

## Getting Started
### Prerequisites
The program is written in Python 3. You can download it from https://www.python.org/downloads/.

Flask framework is used for web functionalities. You can download it from https://pypi.python.org/pypi/Flask/.

SQLAlchemy is used as the ORM. You can download it from http://www.sqlalchemy.org/download.html.

SQLite is used for persistence layer. Please refer to https://www.sqlite.org/index.html.

### Setting up
Initialize the data model with:
```
python3 db_setup.py
```
You should see the direct_booking.db file created afterwards.

Start the web-service with:
```
python3 app.py
```
Please note that to use commit service, the user has to have write access on the .db file.

Default configuration listens from port 5000.

Homepage can be then accessed from http://localhost:$PORT/.

Please refer to `API.md` for API use and testing.

### Styling
PEP8 - Style Guide has been used for the project, please refer to https://www.python.org/dev/peps/pep-0008/.