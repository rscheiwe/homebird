from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import heartbeat, homebird


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

app.include_router(heartbeat.health_router, tags=["Health Check"])
app.include_router(homebird.homes_router, prefix="/homebird", tags=["Home Data"])
