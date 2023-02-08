from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.heartbeat import health_router
from api.homebird import homes_router


def create_app() -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost",
        "http://localhost:8080",
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origins],
        allow_credentials=True,
        allow_methods=["DELETE", "GET", "POST", "PUT"],
        allow_headers=["*"],
    )

    app.include_router(health_router, tags=["Health Check"])
    app.include_router(homes_router, prefix="/homebird", tags=["Home Data"])

    @app.get("/")
    async def root():
        return {
            "name": "Homebird API",
            "version": "1.0.0",
        }

    return app
