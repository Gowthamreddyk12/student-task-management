# Student Task Management System – Serverless Backend

## Overview
This project is a backend application developed using Python to manage student tasks.
It provides REST APIs that allow users to create, view, update, and delete tasks.
The system is designed following serverless architecture principles and cloud-ready design.

---

## System Design
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
```
## Design Choices
  ### Serverless Approach
- No server management required
- Automatic scaling with demand
- Cost-effective for variable workloads

  ### Database Selection
- Fully managed and serverless
- Scales automatically with traffic
- Suitable for key-value access patterns

## Data Validation & Error Handling
- UUID-based task identification
- Input validation using FastAPI models
- Proper HTTP status codes
- Safe handling of invalid IDs and missing fields

## Security Considerations
- IAM roles with least-privilege access
- API Gateway security features (conceptual)

## Scalability Notes
- Automatic Lambda scaling
- High DynamoDB throughput
- Cold start mitigation strategies

## Local Testing
- Tasks are stored in memory for local testing.
- Data resets on server restart and can be replaced with DynamoDB in production.

## Key Learnings
- REST API design using FastAPI
- Serverless backend architecture
- Data handling and validation
- Debugging and environment management

## Summary
This project demonstrates backend development skills, API design,
and cloud-native architecture understanding suitable for real-world applications.
