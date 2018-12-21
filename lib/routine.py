from lib.questions import question_admin
from lib.util import filehandling
from lib.terminal import exam_env, idle_env

class Routine():
    '''
    Main Routine that initializes and setup the questions, 
    saves and loads the questions;
    handles manipulations of questions;
    handles output
    '''
    def __init__(self, path):
        self.fh = filehandling.FileHandlerJson(path)
        self.save_data = self._handle_first_loading()
        self.qa = question_admin.QuestionAdmin(self.save_data)

        self.exam_env = exam_env.TerminalExamEnvironment()
        self.idle_env = idle_env.TerminalIdleEnvironment()

    def show(self):
        for question in self.qa.questions:
            self.qa.show_question(question)

    def idle(self):
        while True:
            command = self.idle_env.start()
            if command =='s' or command == 'S':
                self.save()
                print('Saving finished!')
            elif command == 'l' or command == 'L':
                self.load()
                print('Loading finished!')
            elif command == 'e' or command == 'E':
                print('Yay, editing')
            elif command == 'd' or command == 'D':
                print('Oh nooooo, not deleting')
            elif command == 'a' or command == 'A':
                print('Try to add a question, I dare you')
            elif command == 't' or command == 'T':
                print('Terminating ...')
                return 0
            elif command == 'g' or command == 'G':
                print('STARTING EXAM')
                res = self.start_exam_env()
                command = self._handle_result(res)
            if type(command) == list:
                if (command[0] == 'd' or command[0] == 'D'):
                    self.qa.delete_question(command[1])
                elif (command[0] == 'e' or command[0] == 'E'):
                    print('I want to edit question {}'.format(command[1]))
                elif (command[0] == 'c' or command[0] == 'C'):
                    print('Questioning cancled.')

    def start_exam_env(self):
        questions = self.qa.select_questions()
        result = self.exam_env.start(questions)
        return result

    def save(self):
        self.fh.save_data(self.qa.get_data())

    def load(self, path=''):
        if path:
            self.fh.change_path(path)
        self.save_data = self.fh.load_data()
        self.qa = question_admin.QuestionAdmin(self.save_data)

    def search(self, search=''):
        questions = self.qa.search(search)
        self._show_search_results(questions, search)
        # there could be more later on, for now:
        # just show them on terminal

    def _show_search_results(self, questions, search):
        print('The search results are in; following questions have been found containing {}:'.format(search))
        for q in questions:
            print(str(q.title) + ' in category ' + str(q.category))

    def _handle_first_loading(self):
        try:
            return self.fh.load_data()
        except FileNotFoundError:
            self.fh.save_dummy_data()
            return self.fh.load_data()

    def _handle_result(self, result):
        if type(result) != tuple:
            # print summary or smth
            return 1
        return result
