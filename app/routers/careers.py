from fastapi import APIRouter

router = APIRouter()

@router.get("/careers")
async def get_careers() -> dict:
    return {
        "application": "CareerPilot AI",
            "available_roles": [
                "AI Engineer",
                "Python Developer",
                "Software Engineer",
            ]
        }