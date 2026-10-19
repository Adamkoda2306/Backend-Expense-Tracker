import dotenv
dotenv.load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.general import health, db_health

app = FastAPI(
    title="Expense Tracker",
    version="1.0.0",
    description="Backend API for the Expense Transactions using FastAPI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(db_health.router, prefix="/api/v1", tags=["Health"])


@app.get("/")
def root():
    return { "status": "ok", "message": "Expense Tracker Backend! Visit /docs for Swagger UI" }
