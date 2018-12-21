class TerminalIdleEnvironment():
    def __init__(self):
        self.dummy = None
        self.initial = True

    def start(self):
        if self.initial:
            self._introduction()
            self.initial = False
        self._show_possibilities()
        return self._handle_commands()

    def _introduction(self):
        print('Starting QandA ...')
        print('Welcome to the QandA - Tester (CLI-Edition)!')

    def _show_possibilities(self):
        print('Chose what you want to do:')
        print('- --'*20)
        print('Start exam (G) - Save (S) - Load (L) - Edit questions (E) - Delete questions (D) - Add questions (A) - Terminate (T)')

    def _handle_commands(self):
        command = input()
        while True:
            if command not in ('a', 'A', 'g', 'G', 'd', 'D', 
                    'e', 'E', 'l', 'L', 's', 'S', 't', 'T'):
                command = input('{} is not a valid input!'.format(command))
            return command
