from pathlib import Path

from pypdf import PdfReader

from claims_agent.models.claim_document import ClaimDocument


def load_pdf(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)

        pages_text: list[str] = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages_text.append(text)

        return "\n".join(pages_text)

    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    except Exception as error:
        raise RuntimeError(f"Failed to load PDF: {pdf_path}") from error


def load_claim_documents(claim_number: str) -> list[ClaimDocument]:
    dir_path = Path("data/claims")
    claim_path = dir_path / claim_number

    print(claim_path)
    files = list(claim_path.glob("*.pdf"))
    print(files)
    return []


def main():
    load_claim_documents("CLM-2026-08421")


if __name__ == "__main__":
    main()
