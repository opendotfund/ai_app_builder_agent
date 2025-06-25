# AI App Builder Agent

This project is an agentic AI system that takes a user's prompt for a phone application idea and builds the app for them. It supports two workflows:

- **iOS (Swift)**: Default for general prompts unless otherwise specified or if the app is already in a non-iOS format. Uses DeepSeek V3, Claude, and Gemini agents. Heavy emphasis on beautiful UI and speed.
- **Android (Flutter/React)**: Default is Flutter unless React is specified. Uses Claude, ChatGPT, and Gemini agents.

## Features
- Agent selection for different app build stages
- Prompt history tracking for context chaining
- Automatic debugging and error checking
- Final review and debug of all generated code

## Usage
1. Provide a prompt describing your app idea.
2. The agent will select the appropriate workflow and agents, generate the code, debug, and review it.

---

## Directory Structure
- `main.py`: Entry point
- `agent_framework/`: Core logic for agent orchestration
- `workflows/`: iOS and Android workflow implementations
- `utils/`: Utilities for prompt history, error checking, etc.
