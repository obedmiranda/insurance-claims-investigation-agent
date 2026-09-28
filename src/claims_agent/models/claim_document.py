from pydantic import BaseModel


class ClaimDocument(BaseModel):
    document_id: str
    file_name: str
    content: str
