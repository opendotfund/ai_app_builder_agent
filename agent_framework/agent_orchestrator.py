import sys
from workflows.ios_workflow import IOSWorkflow
from workflows.android_workflow import AndroidWorkflow
from utils.prompt_history import PromptHistory
from utils.error_checker import ErrorChecker

class AgentOrchestrator:
    def __init__(self):
        self.prompt_history = PromptHistory()
        self.error_checker = ErrorChecker()

    def run(self, prompt: str):
        self.prompt_history.add(prompt)
        platform, framework = self._determine_platform(prompt)
        if platform == "ios":
            workflow = IOSWorkflow(self.prompt_history, self.error_checker)
        else:
            workflow = AndroidWorkflow(self.prompt_history, self.error_checker, framework)
        workflow.build_app(prompt)

    def _determine_platform(self, prompt):
        prompt_lower = prompt.lower()
        if "android" in prompt_lower or "flutter" in prompt_lower or "react" in prompt_lower:
            if "react" in prompt_lower:
                return "android", "react"
            return "android", "flutter"
        return "ios", "swift"
