from fastapi import FastAPI

from app.core.config import get_settings

from app.db.session import database_connection

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered resume and job matching API",
    debug=settings.debug,
)


@app.get("/health")
def health_check():
    db_connected = database_connection()

    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "version": settings.app_version,
        "database_connected": db_connected,
    }
