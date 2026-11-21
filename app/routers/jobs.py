from fastapi import APIRouter

router = APIRouter()

@router.get("/jobs")
async def get_jobs() -> list[dict[str, object]]:
    return [
        {
            "id": 1,
            "title": "AI Engineer Intern",
            "company": "Tech Innovations",
            "location": "Bengaluru",
            "required_skills": ["Python", "LLMs", "FastAPI"],
        },
        {
            "id": 2,
            "title": "Python Backend Developer",
            "company": "Cloud Systems",
            "location": "Remote",
            "required_skills": ["Python", "FastAPI", "PostgreSQL"],
        },
        {
            "id": 3,
            "title": "Machine Learning Engineer",
            "company": "Data Labs",
            "location": "Hyderabad",
            "required_skills": ["Python", "TensorFlow", "Machine Learning"],
        },
    ]