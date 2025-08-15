#!/bin/sh

alembic upgrade heads

fastapi run --host 0.0.0.0 --port 8000