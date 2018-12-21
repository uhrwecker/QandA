class TerminalExamEnvironment():
    '''
    Class that handles the exam environment on terminal
    '''
    def __init__(self):
        self.dummy = None

    def start(self, questions):
        result = []
        for q in questions:
            answer_indizes = self._print_question(q, questions.index(q), len(questions))
            answer = self._handle_input(len(answer_indizes))
            if type(answer) == str:
                return (answer, q)
            current_result = self._check_result(answer, q)
            result.append(current_result)
            self._show_result(current_result)
        self._show_result(result)
        return result

    def _print_question(self, q, nb_q, max_nb_q):
        indizes = q.show_on_terminal(nb_q+1, max_nb_q)
        print('- '*40)
        print('Chose one answer! Give the index of the answer(s) {}, that you think are correct.'.format(indizes))
        print('- '*40)
        print('Delete (D) - Edit (E) - Cancel (C) - Submit (ENTER)')
        return indizes

    def _handle_input(self, max_nb_a):
        command = input()
        while True:
            if not command:
                command = input('You have to specifiy an answer or command! \n')
            if command not in ('D', 'd', 'E', 'e', 'C', 'c'):
                try:
                    answer_id = [float(x) for x in command.split(',')]
                    for aid in answer_id:
                        if aid > max_nb_a:
                            raise ValueError
                    return answer_id
                except:
                    command = input('That was not a valid answer or command! \n')
            else:
                return command

    def _check_result(self, answer, q):
        return q.verify(answer)

    def _show_result(self, result):
        # result of form {nb: (bool, comment)} 
        if type(result) == dict:
            # current result
            for index in result:
                print('-- -'*20)
                print('You chose answer {}; that was {}.'.format(index, result[index][0]))
                if result[index][1]:
                    print(result[index][1])

        if type(result) == list:
            for r in result:
                print('Summary for Question No. {}'.format(result.index(r)+1))
                for index in r:
                    print('-- -'*20)
                    print('You chose answer {}; that was {}.'.format(index, r[index][0]))
                    if r[index][1]:
                        print(r[index][1])

        print('-'*80)


