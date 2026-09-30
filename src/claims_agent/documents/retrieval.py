from claims_agent.documents.loader import load_claim_documents
from claims_agent.models.retrieved_evidence import RetrievedEvidence


def _chunk_text(text: str, size: int, overlap: int) -> list[str]:
    position = 0
    chunked_text: list[str] = []

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

    documents = load_claim_documents(claim_number)

    for document in documents:
        chunks = _chunk_text(document.content, 500, 100)

        print(chunks)

    return []


def main():
    results = search_claim_documents(
        claim_number="CLM-2026-08421",
        query="previous plumbing leak",
    )

    print("Results:", results)


if __name__ == "__main__":
    main()
