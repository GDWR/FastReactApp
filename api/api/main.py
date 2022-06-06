from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

COUNTER = 0

router = APIRouter(prefix="/api")

@router.post("/counter")
async def increment_counter():
    global COUNTER
    COUNTER += 1

@router.get("/counter")
async def get_counter() -> int:
    return COUNTER


api.include_router(router)
