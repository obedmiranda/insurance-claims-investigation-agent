from agents import function_tool

from claims_agent.documents.retrieval import search_claim_documents
from claims_agent.models.retrieved_evidence import RetrievedEvidence


@function_tool
def search_claim_documents_tool(
    claim_number: str,
    query: str,
) -> list[RetrievedEvidence]:
    """
    Search the documents associated with an insurance claim for evidence
    relevant to an investigation query.

    Args:
        claim_number: The claim number whose documents should be searched.
        query: A concise description of the evidence to search for.
    """
    return search_claim_documents(
        claim_number=claim_number,
        query=query,
    )
