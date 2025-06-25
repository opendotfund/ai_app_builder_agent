class PromptHistory:
    def __init__(self):
        self.history = []

    def add(self, prompt):
        self.history.append(prompt)

    def get_history(self):
        return self.history
