class Solution(object):
    def isPalindrome(self, x):
        string = str(x)
        if len(string)==1:
            return True
        return string == string[::-1]
        """
        :type x: int
        :rtype: bool
        """