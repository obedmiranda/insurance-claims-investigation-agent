# Insurance Claims Investigation Agent

An AI agent for evidence-backed investigation of insurance claims using document intelligence, retrieval, tool orchestration, and verification.

## Overview

This project explores how AI agents can assist insurance claims adjusters by investigating claim evidence across multiple documents while preserving evidence traceability and identifying conflicting or missing information.

The system is designed to support human investigation, not replace the claims adjuster or make final coverage decisions.

## Synthetic Claim Data

The repository includes synthetic insurance claim documents for development and testing.

The initial case, `CLM-2026-08421`, represents a residential water-damage claim and includes:

* First Notice of Loss (FNOL)
* Homeowner statement
* Property repair history
* Property inspection report
* Relevant insurance policy excerpts

The documents intentionally contain incomplete and potentially conflicting information to support testing of evidence retrieval, conflict detection, provenance, and verification.

All claim data included in this repository is fictional. Real customer, policyholder, or insurance claim data should never be committed to this repository.
## Current Status

The project currently includes:

- An initial Claims Investigator agent built with the OpenAI Agents SDK.
- A PTCF-based system prompt defining the investigator's role and operational boundaries.
- A synthetic residential water-damage claim dataset for development and testing.

The next milestone is document ingestion, allowing the system to extract and access evidence directly from claim documents.
