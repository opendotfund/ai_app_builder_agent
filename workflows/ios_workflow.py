from utils.agent_selector import IOSAgentSelector

class IOSWorkflow:
    def __init__(self, prompt_history, error_checker):
        self.prompt_history = prompt_history
        self.error_checker = error_checker
        self.agent_selector = IOSAgentSelector()

    def build_app(self, prompt):
        print("[iOS Workflow] Building app in Swift...")
        # 1. Decide which agent to use for UI, logic, etc.
        ui_agent = self.agent_selector.select_agent("ui")
        logic_agent = self.agent_selector.select_agent("logic")
        # 2. Generate UI code
        ui_code = ui_agent.generate_ui(prompt)
        # 3. Generate logic code
        logic_code = logic_agent.generate_logic(prompt)
        # 4. Error checking
        self.error_checker.check(ui_code)
        self.error_checker.check(logic_code)
        # 5. Final review
        self.agent_selector.select_agent("review").review([ui_code, logic_code])
        print("[iOS Workflow] App build complete.")
