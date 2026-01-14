# Student Task Management System – Serverless Backend

## Overview
This project is a backend application developed using Python to manage student tasks.
It provides REST APIs that allow users to create, view, update, and delete tasks.
The system is designed following serverless architecture principles and cloud-ready design.

---

## System Design
The application follows a serverless flow:

Client → API Gateway → AWS Lambda (Python / FastAPI) → DynamoDB

For local development and testing, DynamoDB functionality is simulated using an in-memory Python data store.

---

## Technologies Used
- Python 3
- FastAPI
- AWS Lambda (conceptual)
- Amazon API Gateway (conceptual)
- Amazon DynamoDB (conceptual, locally simulated)
- Uvicorn (development server)

---

## Available APIs

| HTTP Method | Endpoint | Purpose |
|------------|----------|---------|
| POST | /task | Create a new task |
| GET | /tasks | Retrieve all tasks |
| GET | /task/{task_id} | Retrieve a task by ID |
| PUT | /task/{task_id} | Update task status |
| DELETE | /task/{task_id} | Remove a task |

---

## Task Structure
```json
{
  "task_id": "uuid",
  "title": "Learn AWS Lambda",
  "description": "Practice serverless development",
  "status": "Pending | In Progress | Completed",
  "created_at": "timestamp"
}

Design Choices
Serverless Approach
No server management required

Automatic scaling with demand

Cost-effective for variable workloads

Database Selection
DynamoDB is preferred because:

It is fully managed and serverless

Scales automatically with traffic

Works well for key-value access patterns

Data Validation & Error Handling
Each task is assigned a UUID

Input validation is handled using FastAPI models

Proper HTTP status codes are returned

Invalid task IDs and missing fields are handled safely

Security Considerations
AWS IAM roles manage service permissions

Least-privilege access is followed

API Gateway can support authentication and throttling (conceptual)

Scalability Notes
AWS Lambda scales automatically with incoming requests

DynamoDB supports high read/write throughput

Cold start impact can be reduced using provisioned concurrency

Serverless model minimizes cost during low usage

Local Testing
For development and testing, tasks are stored in memory using a Python dictionary.
Data is cleared when the server restarts.
This setup can be replaced with real DynamoDB without changing API logic.

Key Learnings
Building REST APIs using FastAPI

Understanding serverless backend architecture

Managing application state and data flow

Debugging Python and environment issues

Summary
This project demonstrates practical backend development skills, REST API design,
and cloud-native architecture understanding suitable for real-world applications.
