# API REST Profesional - Gestion de Tareas

API REST construida con FastAPI + SQLAlchemy, con autenticacion JWT, CRUD completo de tareas, filtros, paginacion y documentacion OpenAPI.

## Caracteristicas

- Registro e inicio de sesion con JWT (`/api/v1/auth/*`)
- CRUD de tareas por usuario autenticado (`/api/v1/tasks`)
- Filtros por estado, prioridad y busqueda por titulo
- Paginacion con `skip` y `limit`
- Validacion robusta con Pydantic
- Documentacion interactiva en Swagger (`/docs`)

## Requisitos

- Python 3.11+

## Instalacion

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

## Ejecucion

```bash
uvicorn app.main:app --reload
```

## Endpoints principales

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login` (OAuth2 form)
- `POST /api/v1/tasks`
- `GET /api/v1/tasks?skip=0&limit=20&status=pending&priority=high&search=report`
- `GET /api/v1/tasks/{task_id}`
- `PATCH /api/v1/tasks/{task_id}`
- `DELETE /api/v1/tasks/{task_id}`
- `GET /health`

## Ejemplo rapido de flujo

1. Registrar usuario.
2. Iniciar sesion con email/password y obtener `access_token`.
3. Enviar `Authorization: Bearer <token>` en endpoints de tareas.
