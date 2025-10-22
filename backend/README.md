# NeuroSense AI Backend

NeuroSense is a web application designed to analyze emotions through various inputs such as facial expressions, voice sentiment, and typing behavior. This backend project is built using Python and Flask, providing a robust API for the frontend to interact with.

## Project Structure

The project follows a modular structure, separating concerns into different directories:

- **src/**: Contains the main application code.
  - **config/**: Configuration files for database and cloud services.
  - **controllers/**: Logic for handling requests and responses for different functionalities.
  - **models/**: Data models representing the application's entities.
  - **routes/**: API route definitions for different functionalities.
  - **services/**: Business logic and interactions with external services.
  - **utils/**: Utility functions for logging, validation, and encryption.
  - **app.py**: Main entry point for the application.
  - **server.py**: Server configuration and startup.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd neurosense-ai-backend
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

4. **Set up environment variables**:
   Create a `.env` file in the `src/` directory and add the following variables:
   ```
   MONGO_URI=<your_mongo_db_uri>
   JWT_SECRET_KEY=<your_jwt_secret_key>
   ```

5. **Run the application**:
   ```
   python src/server.py
   ```

## API Specifications

The backend provides several endpoints for interacting with the application:

- **User Authentication**:
  - `POST /api/users/register`: Register a new user.
  - `POST /api/users/login`: Log in an existing user.

- **Emotion Analysis**:
  - `POST /api/emotions/analyze`: Analyze facial emotions.
  - `POST /api/voice/analyze`: Analyze voice sentiment.

- **Typing Behavior**:
  - `POST /api/typing/analyze`: Analyze typing behavior (if implemented).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.