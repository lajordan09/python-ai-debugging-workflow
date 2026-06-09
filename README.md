# Python AI Debugging Workflow

## AI-Powered Debugging and Refactoring

This repository contains my solution for the Datacom AI-Powered Debugging and Refactoring Simulation. It demonstrates a structured, professional approach to diagnosing and fixing a legacy Python data processing script (`process_data.py`) that was intermittently failing and missing service-level agreement (SLA) performance targets. 

By leveraging AI tools as a technical co-pilot, this project highlights core competencies in maintaining and optimizing data pipelines, a critical skill for robust data analytics and engineering.

## 🔍 Project Objectives

* **Codebase Comprehension:** Analyze and document the functionality of undocumented legacy Python code.
* **Root-Cause Analysis:** Diagnose critical bugs by analyzing system logs and execution tracebacks.
* **Test-Driven Fixing:** Develop a targeted, failing unit test (`TEST_CASES.py`) to reliably reproduce the issue before altering the code.
* **Performance Optimization:** Refactor inefficient logic (e.g., O(N^2) nested loops) into highly performant solutions to meet strict SLAs.
* **Continuous Documentation:** Maintain a comprehensive journal (`DEBUG_LOG.md`) detailing the AI prompts, reasoning, and step-by-step workflow.

## 📂 Repository Structure

```text
datacom-debugging-simulation/
├── process_data.py           # The original legacy script containing the bug
├── refractored_function.py   # The isolated, optimized function logic
├── TEST_CASES.py             # Unit tests written to reproduce and validate the fix
├── DEBUG_LOG.md              # Detailed journal of the AI-assisted debugging process
├── README.md                 # Project overview and instructions
└── error.log                 # The sample production error log used for diagnosis


📝 Documentation
Transparency and tracking are critical when utilizing AI for code generation and refactoring.
All debugging notes, diagnostic reasoning,and specific prompts used during this task are
stored in a dedicated file:

DEBUG_LOG.md: A comprehensive, step-by-step journal detailing the AI-assisted debugging
and root-cause analysis workflow.

🛠️ Tools & Technologies Used
Language: Python 3.x

Testing: unittest framework

Development Environment: Visual Studio Code (VS Code)

AI Assistants: * GitHub Copilot Chat (for code context and refactoring)

Google Gemini (for prompt optimization and architectural reasoning)

Core Competencies: AI-Assisted Code Review, Test-Driven Development (TDD), and Pipeline Optimization

Context: Datacom Job Simulation on Forage - Task 1


