# Library Management App

A Flask-based library management application with CI/CD pipeline using GitHub Actions and Docker containerization.

## Features

- Add books
- Delete books
- Update book information
- Search for books
- List all books
- CORS enabled for cross-origin requests

## Tech Stack

- **Backend**: Flask (Python 3.11)
- **Container**: Docker
- **Orchestration**: Docker Compose (optional)
- **CI/CD**: GitHub Actions
- **Web Server**: Gunicorn

## Local Development

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (for containerized development)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lib_app_demo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python lib.py
   ```

   The app will be available at `http://localhost:5000`

## Docker

### Build and Run with Docker

1. **Build the image**
   ```bash
   docker build -t lib_app_demo:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 lib_app_demo:latest
   ```

3. **Using Docker Compose**
   ```bash
   docker-compose up --build
   ```

   To stop:
   ```bash
   docker-compose down
   ```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **On every push/PR**:
   - Sets up Python environment
   - Installs dependencies
   - Runs linting (flake8)
   - Runs tests

2. **On push to main/develop**:
   - Builds Docker image
   - Pushes to GitHub Container Registry (GHCR)
   - Runs security scanning (Trivy)
   - Creates release (main branch only)

### GitHub Secrets

No additional secrets are required - the workflow uses `GITHUB_TOKEN` for authentication.

## API Endpoints

### Add a Book
```bash
POST /books
Content-Type: application/json

{
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "ISBN-123"
}
```

### List All Books
```bash
GET /books
```

### Search Books
```bash
GET /books/search?query=keyword
```

### Update a Book
```bash
PUT /books/<book_id>
Content-Type: application/json

{
  "title": "Updated Title",
  "author": "Updated Author",
  "isbn": "Updated ISBN"
}
```

### Delete a Book
```bash
DELETE /books/<book_id>
```

## Deployment

### Deploy to Docker Registry

The GitHub Actions workflow automatically builds and pushes Docker images to GitHub Container Registry:

```bash
docker pull ghcr.io/<username>/lib_app_demo:latest
docker run -p 5000:5000 ghcr.io/<username>/lib_app_demo:latest
```

### Environment Variables

- `FLASK_ENV`: Set to `production` in Docker
- `FLASK_APP`: Set to `lib.py`

## Health Check

The Docker container includes a health check that pings the Flask app every 30 seconds.

## Security

- Trivy vulnerability scanning on every push
- Python code linting with flake8
- Code quality checks in CI pipeline

## License

MIT

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request
4. GitHub Actions will automatically test your changes
