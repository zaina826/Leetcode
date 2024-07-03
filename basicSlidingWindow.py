class Solution(object):
    def findMaxAverage(self, nums, k):
        sum=0
        if k==1:
            return(max(nums))
        for i in range(k):
            sum += nums[i]
        curr_sum= sum
        for i in range(len(nums)-k):
            curr_sum = curr_sum+nums[i+k]-nums[i]
            sum=max(curr_sum, sum)
        return((sum*1.0/k))