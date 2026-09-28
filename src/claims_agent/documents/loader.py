from pypdf import PdfReader


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


def main():
    text = load_pdf("data/claims/01_FNOL_Claim_Report.pdf")
    print(text)


if __name__ == "__main__":
    main()
