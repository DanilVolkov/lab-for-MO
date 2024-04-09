class FuncParser:
    def func_pars(self, s):
        answ = []
        arg = False
        num_of_x = ''
        nums = set()
        for i in range(len(s)):
            if s[i] == 'x':
                answ.append('x[')
                arg = True
            elif s[i].isdigit():
                num_of_x+=s[i]
            elif s[i].isdigit() == False and arg == True:
                answ.append(str(int(num_of_x) - 1) +']')
                nums.add(int(num_of_x))
                arg = False
                num_of_x = ''
                if s[i] == '^':
                    answ.append('**')
                else:
                    answ.append(s[i])
            elif s[i].isdigit() == False:
                if len(num_of_x) > 0:
                    answ.append(num_of_x + s[i])
                    num_of_x = ''
                elif s[i] == '^':
                    answ.append('**')
                else:
                    answ.append(s[i])
        if arg == True:
            answ.append(str(int(num_of_x) - 1) +']')
            nums.add(int(num_of_x))
        if len(num_of_x) > 0:
            answ.append(num_of_x)
            num_of_x = ''
            
            
        return len(nums), ''.join(answ)
    