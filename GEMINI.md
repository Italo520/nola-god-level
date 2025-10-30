# GEMINI.md

## Project Overview

This project, "Nola Analytics," is a business intelligence (BI) platform specifically designed for restaurant owners. The goal is to provide a user-friendly interface for exploring and analyzing operational data without requiring technical expertise. The platform allows users to create custom dashboards, build queries visually, and generate various data visualizations to gain insights into their business.

The project is a submission for the "God Level Coder Challenge."

**Technologies:**

*   **Backend:** Python (Django)
*   **Frontend:** React (Create React App or Next.js)
*   **Database:** PostgreSQL
*   **Data Visualization:** ECharts.js
*   **Containerization:** Docker

## Building and Running

The project is containerized using Docker and managed with `docker-compose`.

**To build and run the project:**

1.  **Build the data generator:**
    ```bash
    docker compose build --no-cache data-generator
    ```

2.  **Start the PostgreSQL database:**
    ```bash
    docker compose up -d postgres
    ```

3.  **Generate the data:**
    ```bash
    docker compose run --rm data-generator
    ```
    This process will take 5-15 minutes to generate 500,000 sale records.

4.  **Verify data generation:**
    ```bash
    docker compose exec postgres psql -U challenge challenge_db -c 'SELECT COUNT(*) FROM sales;'
    ```
    This should return a count of around 500,000.

5.  **Start the pgAdmin service (optional):**
    ```bash
    docker compose --profile tools up -d pgadmin
    ```
    pgAdmin will be available at `http://localhost:5050`.

**TODO:** The commands to run the actual front-end and back-end applications are not explicitly defined. Based on the PRD, the backend is a FastAPI application and the frontend is a React application. The following commands are likely to be used:

*   **Backend (FastAPI):** `uvicorn main:app --reload`
*   **Frontend (React):** `npm start`

## Development Conventions

*   **Backend:** The backend is written in Python using the Django Restframework.
*   **Frontend:** The frontend is a React application.
*   **Database:** The project uses a PostgreSQL database. The schema is defined in `database-schema.sql`.
*   **Containerization:** The entire development environment is containerized using Docker.
*   **Code Style:** UI in Brazilian Portuguese, code in English.
