# Insurance Claims Investigation Agent

An AI agent for evidence-backed investigation of insurance claims using document intelligence, retrieval, tool orchestration, and verification.

## Overview

This project explores how AI agents can assist insurance claims adjusters by investigating claim evidence across multiple documents while preserving evidence traceability and identifying conflicting or missing information.

The system is designed to support human investigation, not replace the claims adjuster or make final coverage decisions.

## Synthetic Claim Data

The repository includes synthetic insurance claim documents for development and testing.

The initial case, `CLM-2026-08421`, represents a residential water-damage claim and includes:

- First Notice of Loss (FNOL)
- Homeowner statement
- Property repair history
- Property inspection report
- Relevant insurance policy excerpts

The documents intentionally contain incomplete and potentially conflicting information to support testing of evidence retrieval, conflict detection, provenance, and verification.

All claim data included in this repository is fictional. Real customer, policyholder, or insurance claim data should never be committed to this repository.

## Current Status

The project currently includes:

- An initial Claims Investigator agent built with the OpenAI Agents SDK.
- A PTCF-based system prompt defining the investigator's role and operational boundaries.
- A synthetic residential water-damage claim dataset for development and testing.
- PDF document ingestion into structured `ClaimDocument` models.
- Initial document retrieval infrastructure.
- Fixed-size document chunking with configurable overlap and parameter validation.

The current milestone is building the retrieval layer that will identify relevant evidence across claim documents while preserving its source.

### Document Chunking

The retrieval layer currently splits extracted document text into fixed-size chunks with overlap.

Overlap is used to preserve context that may otherwise be lost at chunk boundaries.

Chunking parameters are validated to prevent invalid configurations such as negative overlap or overlap greater than or equal to the chunk size.

## Project Structure

```text
src/claims_agent/
├── agents/       # AI agents responsible for claim investigation
├── documents/    # Document loading, chunking, and retrieval
└── models/       # Structured data models used across the system

data/claims/      # Synthetic claim documents used for development
tests/            # Automated tests
output/           # Generated investigation reports
