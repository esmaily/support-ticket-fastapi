from fastapi import APIRouter
from auth.router import api_router as api_auth
from ticket.router import api_router as api_ticket

router = APIRouter()
router.include_router(api_auth, prefix="/auth", tags=["auth"])
router.include_router(api_ticket, prefix="/ticket", tags=["ticket"])

