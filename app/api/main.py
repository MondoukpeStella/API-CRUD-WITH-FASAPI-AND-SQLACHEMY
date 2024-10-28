from fastapi import APIRouter
from app.api.routes import user, login, client, measurement

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router,prefix="/users", tags=["users"])
api_router.include_router(client.router,prefix="/clients", tags=["clients"])
api_router.include_router(measurement.router,prefix="/measurements", tags=["measurements"])
