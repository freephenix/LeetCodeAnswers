class Solution(object):
    result_list = []
    def generateParenthesis(self, n):
        global result_list
        def generate(s):
            global result_list
            new_s = s
            left = right = 0
            for i in range(n * 2):
                if s[i] == '(':
                    left += 1
                else:
                    right += 1
                    if left > right and s[i - 1] == '(':
                        new_s = s[:i - 1] + s[i:i + 1] + s[i - 1:i] + s[i + 1:]
                        if new_s not in result_list:
                            result_list += [new_s]
                            generate(new_s)
        s = '(' * n + ')' * n
        result_list = [s]
        generate(s)
        return result_list