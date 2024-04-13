class FuncParser:
    @staticmethod
    def func_pars(s):
        answ = []
        arg = False
        num_of_x = ''
        nums = set()
        for c in s:
            if c == 'x':
                answ.append('x[')
                arg = True
            elif c.isdigit():
                num_of_x += c
            elif not c.isdigit() and arg:
                answ.append(str(int(num_of_x) - 1) + ']')
                nums.add(int(num_of_x))
                arg = False
                num_of_x = ''
                if c == '^':
                    answ.append('**')
                else:
                    answ.append(c)
            elif not c.isdigit():
                if len(num_of_x) > 0:
                    answ.append(num_of_x + c)
                    num_of_x = ''
                elif c == '^':
                    answ.append('**')
                else:
                    answ.append(c)
        if arg:
            answ.append(str(int(num_of_x) - 1) + ']')
            nums.add(int(num_of_x))
        if len(num_of_x) > 0:
            answ.append(num_of_x)
            num_of_x = ''
        return len(nums), ''.join(answ)
