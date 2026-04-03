# Finance Data Processing Backend

## Overview
A modular, production-grade FastAPI backend for finance data processing with:
- User & role management (RBAC)
- Financial transaction CRUD
- Dashboard aggregation APIs
- Secure, validated data flow

## Features
- Domain-driven design: core, api, modules, repositories, services, policies, schemas
- Repository pattern for all DB access
- Service layer for business logic
- Centralized RBAC (roles/permissions)
- SQL aggregation for dashboard (no in-memory loading)
- Pydantic validation, unified error format
- Logging, rate limiting, secure headers, CORS
- JWT authentication (access/refresh), bcrypt password hashing
- Audit logging (CRUD, auth, role changes)
- Environment-based config via .env

## Quickstart
1. Clone repo & install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set up environment variables in `.env` (see sample in repo)
3. Run DB migrations:
   ```sh
   alembic upgrade head
   ```
4. Start the server:
   ```sh
   uvicorn core.app:app --reload
   ```

## API Structure
- `/users/` - User registration, listing, details
- `/transactions/` - CRUD, filtering, pagination
- `/dashboard/` - Aggregated financial data

## Security
- All endpoints require authentication (JWT)
- RBAC enforced via policies
- Secure headers, strict CORS, rate limiting
- No sensitive data exposure
- All secrets in .env

## Testing
- Run tests with:
   ```sh
   pytest
   ```
- Tests cover RBAC and dashboard aggregation

## Extending
- Add routers/services for new modules
- Swap DB or cache with minimal changes
- Integrate with frontend (React, etc.)

## See system_arch.md for full architecture and security details.
