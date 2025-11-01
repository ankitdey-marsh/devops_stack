# Flask Project

This is a simple Flask project that demonstrates how to set up a basic web application with endpoints.

## Project Structure

```
backend_server
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── views.py
├── tests
│   └── test_routes.py
├── config.py
├── requirements.txt
├── run.py
├── Dockerfile
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd backend_server
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python run.py
   ```

## Usage

Once the application is running, you can access the endpoints defined in `app/routes.py`. The root endpoint will return a welcome message.

## Testing

To run the tests, ensure you have installed the testing framework and run:
```
pytest tests/test_routes.py
```

## Docker

To build and run the Docker container, use the following commands:
```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## License

This project is licensed under the MIT License.