from utils.agent_selector import AndroidAgentSelector

class AndroidWorkflow:
    def __init__(self, prompt_history, error_checker, framework="flutter"):
        self.prompt_history = prompt_history
        self.error_checker = error_checker
        self.framework = framework
        self.agent_selector = AndroidAgentSelector(framework)

    def build_app(self, prompt):
        print(f"[Android Workflow] Building app in {self.framework.title()}...")
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
        print("[Android Workflow] App build complete.")
