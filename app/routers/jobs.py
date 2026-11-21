from typing import Any
from fastapi import APIRouter, HTTPException
from app.schemas.jobs import JobResponse

router = APIRouter()

JOBS: list[JobResponse] = [
    JobResponse(
        id=1,
        title="AI Engineer Intern",
        company="Tech Innovations",
        location="Bengaluru",
        required_skills=["Python", "LLMs", "FastAPI"],
    ),
    JobResponse(
        id=2,
        title="Python Backend Developer",
        company="Cloud Systems",
        location="Remote",
        required_skills=["Python", "FastAPI", "PostgreSQL"],
    ),
    JobResponse(
        id=3,
        title="Machine Learning Engineer",
        company="Data Labs",
        location="Hyderabad",
        required_skills=["Python", "TensorFlow", "Machine Learning"],
    ),
]

@router.get("/jobs", response_model=list[JobResponse])
async def get_jobs(location: str | None = None, role: str | None = None) -> list[JobResponse]:
    filtered_jobs = JOBS
    
    if location:
        job_list = []
        for job in filtered_jobs:
            if location.casefold() in job.location.casefold():
                job_list.append(job)
        return job_list
    
    if role:
        job_list = []
        for job in filtered_jobs:
            if role.casefold() in job.title.casefold():
                job_list.append(job)
        return job_list
    
@router.get("/job/{job_id}", response_model=JobResponse)
async def get_job_by_id(job_id: int) -> JobResponse:
    filtered_job = JOBS
    for job in filtered_job:
        if job.id == job_id:
            return job
    
    raise HTTPException(
        status_code=404,
        detail=f"{job_id} not found",
    )   