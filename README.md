# Finance Data Processing System

## Overview

This project is a modular, secure backend system for managing financial data, paired with a lightweight frontend dashboard for interaction.

It is designed to demonstrate strong backend engineering principles including clean architecture, role-based access control (RBAC), secure API design, and efficient data processing.

---

<img width="1443" height="925" alt="image" src="https://github.com/user-attachments/assets/9319c1a7-0892-4cfb-aca6-504c1676c645" />


## Key Features

### Backend

* Modular architecture (core, api, services, repositories, policies)
* Role-Based Access Control (RBAC)
* JWT Authentication (access + refresh tokens)
* Secure API design (no trust on client-provided identity)
* Financial transaction management (CRUD + filtering)
* Dashboard analytics (aggregations using SQL)
* Repository pattern (no direct DB access outside repositories)
* Input validation via Pydantic
* Secure headers, CORS, and rate limiting
* Audit logging for critical operations

### Frontend

* React + Vite application
* Authentication (login/register)
* Dashboard view (financial summaries)
* Transaction listing
* API integration with JWT handling

---

## Project Structure

```
Finiance_proj/
├── core/              # App config, DB, models
├── api/               # Route handlers
├── services/          # Business logic
├── repositories/      # Database access layer
├── schemas/           # Validation models
├── policies/          # RBAC rules
├── modules/           # Auth & dependencies
├── alembic/           # DB migrations
├── frontend/          # React frontend
├── tests/             # Unit tests
```

---

## Architecture Overview

The system follows a layered architecture:

```
Client → API Router → Dependency (Auth)
       → Service Layer → Repository Layer → Database
```

### Key Principles

* No business logic in routers
* No DB access outside repositories
* All requests validated and authorized
* User identity derived strictly from JWT (never from client input)

---

## Security Design

* JWT-based authentication (short-lived access tokens)
* RBAC enforced via centralized policies
* Prevention of privilege escalation (no client-controlled user_id)
* Secure HTTP headers (HSTS, XSS protection, etc.)
* Strict CORS configuration
* Rate limiting on sensitive endpoints
* All queries scoped to authenticated user
* No sensitive data exposure in responses

---

## Getting Started

### Backend Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:

   ```
   cp .env-example .env
   ```

3. Run migrations:

   ```bash
   alembic upgrade head
   ```

4. Start server:

   ```bash
   uvicorn core.app:app --reload
   ```

Backend runs at:

```
http://localhost:8000
```

---

### Frontend Setup

1. Navigate to frontend:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run dev server:

   ```bash
   npm run dev
   ```

Frontend runs at:

```
http://localhost:5173
```

---

## API Endpoints

| Endpoint         | Description         |
| ---------------- | ------------------- |
| `/auth/login`    | User authentication |
| `/users/`        | User management     |
| `/transactions/` | Transaction CRUD    |
| `/dashboard/`    | Financial summaries |

---

## Assumptions

* Authentication is required for all endpoints
* Users can only access their own data unless explicitly permitted
* SQLite is used for simplicity (can be swapped with PostgreSQL)
* Frontend is a thin client (no security logic enforced there)

---

## Tradeoffs

* SQLite used for simplicity over scalability
* LocalStorage used for JWT (instead of HttpOnly cookies)
* Minimal UI to focus on backend architecture
* In-memory rate limiting and caching (not distributed)

---

## Future Improvements

* PostgreSQL + Redis for production readiness
* Role-based UI rendering
* Advanced filtering & analytics
* Distributed rate limiting
* Observability (logging + tracing)
* Secure cookie-based authentication

---

## Testing

Run tests with:

```bash
pytest
```

Focus areas:

* RBAC enforcement
* Data access isolation
* Dashboard aggregation correctness

---

## Documentation

* `system_arch.md` → detailed system design
* `progress.md` → development tracking

---

## Final Notes

This project prioritizes clarity, maintainability, and security over unnecessary complexity. It demonstrates how a backend system should be structured to handle real-world concerns such as access control, data integrity, and modular scalability.

---
