class Solution(object):
    def isSubsequence(self, s, t):
        dynamic_s=s
        
        for letter in t:
            if dynamic_s=="":
                return True
            if dynamic_s[0]==letter:
                dynamic_s=dynamic_s[1:]
        if dynamic_s=="":
            print("true")
            return True
        else:
            print("false")
            return False
idk=Solution
idk.isSubsequence(idk,"b","abc")