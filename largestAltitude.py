class Solution(object):
    def largestAltitude(self, gain):
        altitudes= [0]
        for i in range(len(gain)):
            altitudes.append(gain[i]+altitudes[i])
        return(max(altitudes))
        """
        :type gain: List[int]
        :rtype: int
        """