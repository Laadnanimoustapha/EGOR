---
title: EGOR
emoji: 🔐
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
---

# EGOR

This is the minimal setup for the EGOR application.

## Version 1 - 2026-04-03

![Screenshot Version 1](assests/download%20(1).png)

## System Workflow Diagram

```mermaid
flowchart TD
    %% Define Styles
    classDef client fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef server fill:#10b981,stroke:#fff,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef database fill:#f59e0b,stroke:#fff,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef redis fill:#ef4444,stroke:#fff,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef ai fill:#8b5cf6,stroke:#fff,stroke-width:2px,color:#fff,rx:5px,ry:5px;

    %% Nodes
    Client((Frontend Clients)):::client
    FastAPI[FastAPI Server <br> uvicorn main:app]:::server
    
    subgraph Security & Limits
        Auth{Check API Key}
        RateLimit{Upstash Redis <br> Rate Limiter}:::redis
    end

    subgraph Endpoints
        EP_Gen[/ `/generate` /]
        EP_Sum[/ `/api/summarize` /]
        EP_Health[/ `/health` /]
    end

    DB[(MySQL/Postgres DB <br> via SQLAlchemy)]:::database
    
    subgraph AI Summarizer Waterfall
        AI_Gemini[Gemini]:::ai
        AI_Groq[Groq]:::ai
        AI_HF[HuggingFace Models]:::ai
    end

    %% Connections
    Client -->|HTTPS Request| FastAPI
    FastAPI --> Auth
    Auth -->|Queries API Key| DB
    Auth -->|Invalid| 401[401 Unauthorized]
    Auth -->|Valid| RateLimit
    
    RateLimit -->|Check Limit 60s window| RateLimit
    RateLimit -->|Exceeded Limit| 429[429 Too Many Requests]
    RateLimit -->|Valid Request| Endpoints
    
    EP_Gen -->|Returns| Password[Random Password]
    EP_Health -->|Pings| DB
    
    EP_Sum --> AI_Gemini
    AI_Gemini -->|Fallback if fails| AI_Groq
    AI_Groq -->|Fallback if fails| AI_HF

    Password -.-> Client
    AI_Gemini -.-> Client
    AI_Groq -.-> Client
    AI_HF -.-> Client
    EP_Health -.-> Client
```