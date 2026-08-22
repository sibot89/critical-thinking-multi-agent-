# Critical Thinking with Multi-Agent AI

A small multi-agent system built with **CrewAI** that evaluates claims from two opposing perspectives before producing a balanced final assessment.

## Overview

The project explores how multiple specialized AI agents can collaborate on a reasoning task instead of relying on a single general-purpose agent.

Given a claim, three agents perform different roles:

1. **Skeptic Agent** — identifies logical gaps, unsupported claims, and exaggerations.
2. **Supporter Agent** — identifies plausible arguments, potential benefits, and supporting context.
3. **Synthesizer Agent** — compares both perspectives and produces a balanced evaluation.

## Workflow

    Input Claim
         │
    ┌────┴────┐
    │         │
    ▼         ▼
    Skeptic   Supporter
    Agent     Agent
    │         │
    └────┬────┘
         │
         ▼
    Synthesizer Agent
         │
         ▼
    Balanced Evaluation

## Example

The system evaluates claims such as:

> "Using AI in schools will completely eliminate the need for human teachers by 2030, increasing student learning efficiency by 300%."

The agents independently analyze the claim before the Synthesizer combines their findings into a final report covering:

- Executive Summary
- Strengths and Plausible Arguments
- Weaknesses and Unsupported Claims
- Final Verdict

## Architecture

### 1. Skeptic Agent

Focuses on critical analysis.

**Responsibilities:**

- Identify unsupported assumptions
- Detect logical gaps
- Question exaggerated claims
- Highlight statements requiring stronger evidence

### 2. Supporter Agent

Provides a constructive counter-perspective.

**Responsibilities:**

- Identify plausible aspects
- Find potential benefits
- Provide supporting context
- Explore reasonable interpretations

### 3. Synthesizer Agent

Acts as an objective evaluator.

**Responsibilities:**

- Compare both perspectives
- Weigh conflicting arguments
- Distinguish plausible claims from exaggeration
- Produce the final assessment

## Tech Stack

- Python
- CrewAI
- Google Gemini
- python-dotenv

## Project Structure

    critical-thinking-multi-agent/
    ├── critical_thinking_multi_agent.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

## Setup

### 1. Clone the repository

    git clone https://github.com/sibot89/critical-thinking-multi-agent.git
    cd critical-thinking-multi-agent

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Configure the API key

Create a `.env` file based on `.env.example`:

    GOOGLE_API_KEY=your_google_api_key_here

The `.env` file is intentionally excluded from version control.

### 4. Run

    python critical_thinking_multi_agent.py

## What This Project Demonstrates

This project focuses on **task specialization in multi-agent systems**.

Rather than asking one agent to perform the entire analysis, the reasoning process is divided into specialized roles with different objectives.

The project also served as an exploration of:

- Multi-agent orchestration with CrewAI
- Role-based agent design
- Sequential task execution
- Conflicting-perspective analysis
- LLM-based synthesis

## Limitations

This is an experimental and educational project rather than a production-grade fact-checking system.

The agents evaluate reasoning and plausibility based on the information available to the underlying language model. They do not independently establish factual truth or provide guaranteed verification of claims.

## Future Improvements

Potential extensions include:

- Web-based evidence retrieval
- Source citation and verification
- Structured evaluation scores
- Additional specialized agents
- Human-in-the-loop review

---

Built as an exploration of **multi-agent reasoning and task specialization with CrewAI**.
