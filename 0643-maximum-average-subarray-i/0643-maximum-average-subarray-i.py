class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = sum(nums[:k])
        max_avg = curr_sum / k
        
        for i in range(k,len(nums)):
            curr_sum = curr_sum+nums[i]-nums[i-k]
            curr_avg=curr_sum/k
            max_avg=max(max_avg,curr_avg)
                
        return max_avg
                
                
                
        