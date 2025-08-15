# fastapi-boilerplate

A ready-to-use template for quickly starting new FastAPI projects.  
---


## 📌 Installation & Run Steps

### 1 — Clone the Repository
```bash
git clone https://github.com/faridhaavasi/fastapi-boilerplate.git
cd fastapi-boilerplate
```

### 2 — Create `.env` File
Create a `.env` file in the **root directory** of the project (where `Dockerfile` and `docker-compose.yml` exist) with the following content:

```env
SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/db_name
JWT_SECRET_KEY=supersecretkey
```
