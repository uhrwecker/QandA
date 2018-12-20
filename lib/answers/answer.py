class Answer():
    '''
    Impl. of an Answer;
    check if setting of answer properties is valid;
    store, if answer has a comment (and handle printing);
    store, if answer is correct answer
    '''
    def __init__(self, answer_string='', comment='', is_correct=False):
        assert answer_string, 'Answer Object has to have a description/entry!'
        self.answer_string = answer_string
        self.comment = comment
        self.is_correct = is_correct

    def check_if_correct(self):
        return self.is_correct

    def edit(self, entry, new_value):
        if entry == 'answer_string':
            assert (new_value and type(new_value) == str), 'The new entry for the answer_string must be string of len > 0.'
            self.answer_string = new_value

        elif entry == 'comment':
            assert (new_value and type(new_value) == str), 'The new entry for comments must be string of len > 0.'
            self.comment = new_value

        elif entry == 'is_correct':
            assert type(new_value) == bool, 'The new value for is_correct must be bool'
            self.is_correct = new_value

        else:
            raise ValueError('The entry {} is not in possible answer fields [answer_string, comment, is_correct]'.format(entry))

    def __str__(self):
        return self.answer_string + '\n'
