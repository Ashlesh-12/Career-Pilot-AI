from pydantic import BaseModel

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    required_skills: list[str]