# Support Platform

A FastAPI application scaffold for a support platform. The current API provides
basic root and health-check endpoints.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup

Install the project dependencies from the lockfile:

```bash
uv sync
```

## Run locally

Start the development server with automatic reload:

```bash
uv run fastapi dev app/main.py
```

The API is available at <http://127.0.0.1:8000>. Interactive API documentation
is available at <http://127.0.0.1:8000/docs>.

## Available endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Basic application status |
| `GET` | `/health` | Health-check response |
