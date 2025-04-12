Certainly! Here's how the content would look if we split it into two files:

---

### **`README.md`** (main file):

# litestar_intro

A prototype backend built with [Litestar](https://docs.litestar.dev) for managing users and authentication using JWT. This is my first project with Litestar, and I tried to follow its philosophy and tooling as closely as possible.

User management is based on the [`litestar-users`](https://github.com/litestar-org/litestar-users) plugin. The goal was to explore the Litestar ecosystem and its batteries-included approach compared to alternatives like FastAPI or Django.

---

## 🚀 Features

This project includes a basic user management API:

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/users`           | Get all users       |
| GET    | `/users/{user_id}` | Get user by ID      |
| DELETE | `/users/{user_id}` | Delete user         |
| PATCH  | `/users/{user_id}` | Update user by ID   |
| GET    | `/users/me`        | Get current user    |
| PATCH  | `/users/me`        | Update current user |
| POST   | `/register`        | Register new user   |
| POST   | `/login`           | Obtain JWT token    |

All routes are powered by `litestar-users`, and user data is stored in a PostgreSQL database using async SQLAlchemy.

---

## 🧱 Tech Stack

- **Backend:** Litestar, litestar-users
- **ORM:** SQLAlchemy (async), Alembic (managed by Litestar)
- **Database:** PostgreSQL (via asyncpg)
- **Config:** pydantic-settings
- **Containerization:** Docker, docker-compose

---

## 🛠️ Getting Started

### Run with Docker (Recommended)

```bash
docker-compose up --build
```

- No `.env` required — defaults and overrides are handled via `docker-compose.yml`.
- Ensure ports `8000` and `5432` are free.
- Then you can apply migrations with `litestar database upgrade`, not in docker, it can be done outside to upgrade docker db.

---

## 📌 Notes

This project was created as a prototype and test task, but more importantly, out of personal curiosity toward Litestar.

The test task didn't require the use of `litestar-users`, but I felt that **exploring the full Litestar ecosystem, including its first-party tools, made more sense**. Why ignore the main strengths of the framework you're testing?

I genuinely enjoyed working with Litestar. It hits a sweet spot between Django’s heavy boilerplate and FastAPI’s lack of structured built-ins. The experience felt clean, well-integrated, and fun to use — I see real potential here.
