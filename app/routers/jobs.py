from typing import Any
from fastapi import APIRouter, HTTPException

router = APIRouter()

JOBS: list[dict[str, str | list[str]]] = [
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

@router.get("/jobs")
async def get_jobs(location: str | None = None, role: str | None = None) -> list[dict[str, Any]]:
    filtered_jobs = JOBS
    
    if location:
        job_list = []
        for job in filtered_jobs:
            if location.casefold() in job["location"].casefold():
                job_list.append(job)
        return job_list
    
    if role:
        job_list = []
        for job in filtered_jobs:
            if role.casefold() in job["title"].casefold():
                job_list.append(job)
        return job_list
    
@router.get("/job/{job_id}")
async def get_job_by_id(job_id: int) -> dict[str, Any]:
    filtered_job = JOBS
    for job in filtered_job:
        if job["id"] == job_id:
            return job
    
    raise HTTPException(
        status_code=404,
        detail=f"{job_id} not found",
    )   