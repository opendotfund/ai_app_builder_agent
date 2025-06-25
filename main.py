from agent_framework.agent_orchestrator import AgentOrchestrator
from utils.prompt_history import PromptHistory

if __name__ == "__main__":
    print("Welcome to the AI App Builder Agent!")
    prompt = input("Describe your phone app idea: ")
    orchestrator = AgentOrchestrator()
    orchestrator.run(prompt)
