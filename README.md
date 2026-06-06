# Python AI Debugging Workflow
## Task 1: AI-Powered Debugging and Refactoring

This repository contains my solution to the Datacom AI‑Powered Debugging and Refactoring Simulation on Forage. 
The project simulates a real-world scenario where a legacy Python script (`process_data.py`) intermittently fails and performs below SLA requirements.

## 🔍 Project Objectives
- Understand and document a legacy codebase
- Diagnose a critical bug using logs and traceback analysis
- Write a failing unit test to reproduce the issue
- Refactor and optimize the problematic function
- Validate the fix with automated tests
- Maintain a DEBUG_LOG.md documenting the entire workflow

## 📁 Repository Structure
```
datacom-debugging-simulation/
│
├── process_data.py               # Legacy script (original + refactored)
├── TEST_CASES.py                 # Failing + passing unit tests
├── DEBUG_LOG.md                  # Your documentation journal
├── README.md                     # Project overview
│
├── /logs
│   └── error.log                 # Provided error log
│
├── /analysis
│   └── code_summary.md           # Output from Step 1 (AI analysis)
│
├── /refactor
│   └── refactored_function.py    # Optional: isolated refactor
│
└── /assets
    └── screenshots/              # VS Code screenshots, prompts, etc.


## 🧪 Running Tests
```bash
python -m unittest TEST_CASES.py
```

# 📝 Documentation
All debugging notes, prompts, and reasoning are stored in:
DEBUG_LOG.md

# 🛠 Tools Used
### Python 3.x
### Code Review
### unittest

### VS Code + Copilot Chat
### Google Gemini (Improve prompt)
### Created workflows for future projects

### Forage Datacom Simulation - Task 1 Overview
### Forage Datacom Simulation - Task 2 Overview
### Forage Datacom Simulation - Task 3 Overview

