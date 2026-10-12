from claims_agent.documents.loader import load_claim_documents
from claims_agent.models.retrieved_evidence import RetrievedEvidence


def normalize_text(text: str) -> str:
    return text.lower().strip()


def get_query_terms(query: str) -> list[str]:
    """
    Convert a search query into individual terms for lexical retrieval.

    The query is first normalized and then split by whitespace.

    Example:
        "Previous Plumbing LEAK"
        -> ["previous", "plumbing", "leak"]

    This is a basic lexical approach. It does not currently remove
    stop words, perform stemming, or understand semantic meaning.
    """
    normalized_query = normalize_text(query)
    return normalized_query.split()


def count_matching_terms(text: str, query_terms: list[str]) -> int:
    normalized_text = normalize_text(text)

    return sum(term in normalized_text for term in query_terms)


def chunk_text(text: str, size: int, overlap: int) -> list[str]:
    position = 0
    chunked_text: list[str] = []

    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative")

    if overlap >= size:
        raise ValueError(
            f"Overlap ({overlap}) must be smaller than chunk size ({size})"
        )

    while position < len(text):
        slice_text = text[position : position + size]
        chunked_text.append(slice_text)
        position += size - overlap

    return chunked_text


def search_claim_documents(
    claim_number: str,
    query: str,
) -> list[RetrievedEvidence]:
    """
    Search the documents associated with a claim for evidence relevant
    to an investigation query.

    The retrieval process:
    1. Loads all documents associated with the claim.
    2. Extracts searchable terms from the query.
    3. Splits each document into overlapping text chunks.
    4. Compares each chunk against the query terms.
    5. Selects chunks considered relevant to the query.
    6. Returns the relevant chunks as RetrievedEvidence while preserving
       their source document information.

    This function is responsible for retrieving evidence, not interpreting
    the evidence or making claim investigation decisions.
    """
    documents = load_claim_documents(claim_number)
    query_terms = get_query_terms(query)
    retrieved_evidence: list[RetrievedEvidence] = []

    for document in documents:
        chunks = chunk_text(document.content, 500, 100)

        for chunk in chunks:
            score = count_matching_terms(chunk, query_terms)

            if score > 0:
                evidence = RetrievedEvidence(
                    document_id=document.document_id,
                    file_name=document.file_name,
                    text=chunk,
                )
                retrieved_evidence.append(evidence)

    return retrieved_evidence


def main():
    results = search_claim_documents(
        claim_number="CLM-2026-08421",
        query="previous plumbing leak",
    )

    print("Results:", results)


if __name__ == "__main__":
    main()
