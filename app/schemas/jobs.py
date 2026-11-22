from pydantic import BaseModel

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    required_skills: list[str]
    
class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    required_skills: list[str]
    
class JobUpdate(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    required_skills: list[str] | None = None
    