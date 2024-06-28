class Solution(object):
    def reverseWords(self, s):
        list_of_words=[]
        word=""
        for letter in s:
            if letter!=" ":
                word= word+letter
            else:
                if word:
                    list_of_words.append(word)
                    word=""
        if word:
            list_of_words.append(word)

        final_sentence=""
        for word in reversed(list_of_words):
            final_sentence=final_sentence+word+" "
        print(final_sentence.strip())
        return(final_sentence.strip())
# Testing the reverseWords method
solution = Solution()
  
output = solution.reverseWords("")
