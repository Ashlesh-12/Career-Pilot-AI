from fastapi import APIRouter

router = APIRouter()

@router.get("/careers")
async def get_careers() -> dict[str, str | list[str]]:
    return {
        "application": "CareerPilot AI",
            "available_roles": [
                "AI Engineer",
                "Python Developer",
                "Software Engineer",
            ]
        }