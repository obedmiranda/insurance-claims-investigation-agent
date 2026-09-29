from pydantic import BaseModel


class RetrievedEvidence(BaseModel):
    document_id: str
    file_name: str
    text: str
