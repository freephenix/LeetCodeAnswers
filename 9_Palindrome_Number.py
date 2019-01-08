class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False;

        if len(str(x)) == 1:
            return True;

        for i in range(int(len(str(x))/2)):
            print("1 -- ", int((x % pow(10,i+1)) / pow(10,i)), "\n");
            print("2 -- ", (int(x / pow(10,len(str(x)) - i - 1)) % 10), "\n");

            if(int((x % pow(10,i+1)) / pow(10,i)) != (int(x / pow(10,len(str(x)) - i - 1)) % 10)):
                return False;

        return True;


in_num = input();
num = int(in_num);

solution = Solution();
print(solution.isPalindrome(num));

