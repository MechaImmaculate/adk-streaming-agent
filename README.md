# ADK Streaming Agent — Google Search Integration

This project is a simple implementation of a **Google Search Agent** using the **Google Agent Development Kit (ADK)**.  
It demonstrates how to build, register, and run an AI-powered agent capable of retrieving real-time search information using ADK’s streaming capabilities.

---

## 🧠 Overview

The project defines a `root_agent` that uses the `google_search` tool for live data grounding.  
It is designed as a lightweight example to explore ADK’s structure, tools, and model integration workflow.

### Key Features
- Built with **Google ADK** (Agent Development Kit)  
- Uses **Gemini 2.5 Flash** model for LLM capabilities  
- Integrates the **Google Search Tool** for live information retrieval  
- Supports **streaming** responses for real-time interaction  
- Organized agent structure for modular development

---

## 📁 Project Structure
adk-streaming/
│
├── app/ # Main ADK app folder
├── google_search_agent/ # Custom agent implementation
│ ├── agent/ # Contains the root agent file
│ │ └── root_agent.py
│ ├── init.py
│
├── .env # Environment variables (excluded from Git)
├── .venv/ # Local Python environment (excluded from Git)
