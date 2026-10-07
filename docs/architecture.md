insurance-claims-investigation-agent/
├── data/
├── docs/                  ← nueva
│   └── architecture.md    ← nuevo
├── output/
├── src/
├── tests/
├── README.md
└── ...

## Component Responsibilities

### Document Loader

Loads the PDF documents associated with a claim and converts them into structured `ClaimDocument` objects.

### Document Chunking

Splits extracted document content into smaller overlapping units that can be searched without losing important context around chunk boundaries.

### Document Retrieval

Searches document chunks for information relevant to an investigation query and returns evidence together with its source information.

### Investigation Agent

Uses retrieved evidence to identify relevant facts, potential conflicts, and missing information without making final coverage or claim decisions.
