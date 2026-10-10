from claims_agent.documents.retrieval import chunk_text, normalize_text


def test_normalize_text():
    text = "  Previous Plumbing LEAK  "

    result = normalize_text(text)

    assert result == "previous plumbing leak"


def test_chunk_text_splits_text_with_overlap():
    text = "ABCDEFGHIJ"

    chunks = chunk_text(
        text=text,
        size=5,
        overlap=2,
    )

    assert chunks == [
        "ABCDE",
        "DEFGH",
        "GHIJ",
        "J",
    ]
