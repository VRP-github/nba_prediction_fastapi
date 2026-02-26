# NBA Player Position Prediction API

A REST API that predicts an NBA player's position based on their statistical performance metrics, powered by a K-Nearest Neighbors machine learning model and served via FastAPI.

## Overview

This service accepts a set of basketball statistics for a player and returns a predicted position (e.g., Guard, Forward, Center). The model was trained on historical NBA player data and is served through a lightweight, high-performance FastAPI application.

## Features

- **ML-powered predictions** using a pre-trained K-Nearest Neighbors (KNN) model
- **Input validation** via Pydantic schemas
- **Automatic API docs** at `/docs` (Swagger UI) and `/redoc` (ReDoc)
- **Docker support** for containerized deployment
- **MIT licensed**

## Project Structure

```
nba_prediction_fastapi/
├── app/
│   ├── app.py                  # FastAPI application and route definitions
│   └── schemas/
│       └── data_validation.py  # Pydantic input validation schema
├── model/
│   ├── nba_knn.joblib          # Pre-trained KNN model
│   └── position_labels.joblib  # Label encoder for position classes
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
└── Dockerfile                  # Docker configuration
```

## Requirements

- Python 3.12+
- pip

## Installation

1. **Clone the repository**

   ```bash
   https://github.com/VRP-github/nba_prediction_fastapi.git
   cd nba_prediction_fastapi
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate       # macOS/Linux
   .venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

**Option A — Python directly:**

```bash
python main.py
```

**Option B — FastAPI CLI:**

```bash
fastapi run main.py
```

**Option C — Uvicorn:**

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Docker

**Build the image:**

```bash
docker build -t nba-prediction .
```

**Run the container:**

```bash
docker run -p 8000:8000 nba-prediction
```

## API Reference

### `POST /predict`

Predicts a player's position based on their statistics.

**Request Body**

| Field                | Type  | Description                   |
|----------------------|-------|-------------------------------|
| `AST`                | float | Assists                       |
| `STL`                | float | Steals                        |
| `BLK`                | float | Blocks                        |
| `TRB`                | float | Total Rebounds                |
| `FGA`                | float | Field Goals Attempted         |
| `FG_PERCENTAGE`      | float | Field Goal Percentage         |
| `THREE_P`            | float | 3-Pointers Made               |
| `THREE_PA`           | float | 3-Pointers Attempted          |
| `PF`                 | float | Personal Fouls                |
| `eFG_PERCENTAGE`     | float | Effective Field Goal %        |
| `FT_PERCENTAGE`      | float | Free Throw Percentage         |
| `DRB`                | float | Defensive Rebounds            |
| `THREE_P_PERCENTAGE` | float | 3-Point Percentage            |
| `TWO_P`              | float | 2-Pointers Made               |
| `TWO_P_PERCENTAGE`   | float | 2-Point Percentage            |

**Example Request**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "AST": 5.2,
    "STL": 1.3,
    "BLK": 0.4,
    "TRB": 4.1,
    "FGA": 14.0,
    "FG_PERCENTAGE": 0.47,
    "THREE_P": 2.1,
    "THREE_PA": 5.8,
    "PF": 2.2,
    "eFG_PERCENTAGE": 0.55,
    "FT_PERCENTAGE": 0.82,
    "DRB": 3.2,
    "THREE_P_PERCENTAGE": 0.36,
    "TWO_P": 5.7,
    "TWO_P_PERCENTAGE": 0.54
  }'
```

**Example Response**

```json
{
  "prediction": "PG"
}
```

**Error Response (500)**

```json
{
  "error": "<error message>"
}
```

## Interactive API Documentation

Once the server is running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## Tech Stack

| Layer       | Technology                    |
|-------------|-------------------------------|
| API         | FastAPI, Uvicorn, Starlette   |
| Validation  | Pydantic v2                   |
| ML Model    | scikit-learn (KNN), joblib    |
| Numerics    | NumPy, SciPy                  |
| Container   | Docker (python:3.12-slim)     |

## License

This project is licensed under the [MIT License](LICENSE).
