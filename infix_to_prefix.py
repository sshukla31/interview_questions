'''
Infix to Prefix

Reference:
    GeeksForGeeks:
    https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
'''


class Conversion(object):
    def __init__(self):
        self.stack = []
        self.result = []
        self.precedence = {
            "^": 3,
            "/": 2,
            "*": 2,
            "+": 1,
            "-": 1
        }

    def is_operand(self, char):
        return char.isalpha()

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def peek(self):
        return self.stack[-1]

    def infix_to_postfix(self, exp):
        for char in exp:
            if self.is_operand(char):
                self.result.append(char)
            elif char == "(":
                self.stack.append(char)
            elif char == ")":
                while(not self.is_empty() and self.peek()!='('):
                    self.result.append(self.stack.pop())

                if (not self.is_empty() and self.peek() == '('):
                    self.stack.pop()
                else:
                    return -1
            else:
                while(
                    not self.is_empty() and
                    self.peek() != '(' and
                    self.precedence[char] <= self.precedence[self.peek()]
                ):
                    self.result.append(self.stack.pop())

                self.stack.append(char)
            print self.result


        while(not self.is_empty()):
            self.result.append(self.stack.pop())


        print self.result
        return self.result



if __name__=='__main__':
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    obj = Conversion()
    actual_result = obj.infix_to_postfix(exp)
    expected_result = "abcd^e-fgh*+^*+i-"
    assert "".join(actual_result) == expected_result