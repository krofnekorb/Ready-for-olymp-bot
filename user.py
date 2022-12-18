class User:
    def __init__(self, username):
        self.username = username
        self.current_section = ''
        self.progress = dict(
            tfcv=1,
            linal=1,
            calculus=1,
            algebra=1,
            comb=1,
            probability=1
        )

    def update_progress(self):
        current_task = self.progress.get(self.current_section)
        current_task += 1
        self.progress[self.current_section] = current_task
        self.reset_current_section()

    def get_current_task_number(self):
        assert(self.get_current_section() != ''),\
            'Illegal attempt to get current_task with unannounced current_section'
        return self.progress.get(self.current_section)

    def get_current_section(self):
        return self.current_section

    def set_current_section(self, new_section):
        self.current_section = new_section

    def reset_current_section(self):
        self.set_current_section('')

    def get_username(self):
        return self.username
