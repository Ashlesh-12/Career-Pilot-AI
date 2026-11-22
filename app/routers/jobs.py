from typing import Any
from fastapi import APIRouter, HTTPException, status
from app.schemas.jobs import JobResponse, JobCreate, JobUpdate

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
    
    return filtered_jobs
    
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

@router.post("/jobs", response_model=JobResponse, status_code= status.HTTP_201_CREATED,)
async def create_jobs(job_data: JobCreate) -> JobResponse:
    new_id = 0
    for job in JOBS:
        new_id = max(job.id, new_id)
    new_id += 1
    
    new_job = JobResponse(
        id=new_id,
        **job_data.model_dump(),
    )
    
    JOBS.append(new_job)
    return new_job

@router.patch("/jobs/{job_id}", response_model=JobResponse)
async def update_job(job_id: int, job_data: JobUpdate) -> JobResponse:
    updates = job_data.model_dump(
         exclude_unset=True,
         exclude_none=True,
    )
    print(updates)
     
    if not updates:
        raise HTTPException(
            status_code=400,
            detail="At least one non-null field must be provided",
        )
     
    for index, job in enumerate(JOBS):
         if job_id == job.id:
            # merging dictionaries
            updated_data = job.model_dump() | updates
            print(updated_data) 
            # converted back into object
            updated_job = JobResponse(**updated_data)
             
            JOBS[index] = updated_job
            
            return updated_job
    
    raise HTTPException(status_code=404, detail=f"Job with ID {job_id} not found")

@router.delete("/jobs/{job_id}")
async def delete_job(job_id: int, status_code=status.HTTP_204_NO_CONTENT):
    for index, job in enumerate(JOBS):
        if job.id == job_id:
            JOBS.pop(index)
            return
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{job_id} not found")
             