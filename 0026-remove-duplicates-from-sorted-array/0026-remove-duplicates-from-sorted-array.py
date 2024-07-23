class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        curr=nums[0]
        i,j =1,1
        n=len(nums);
        while j < n:
            if nums[j] != curr:
                curr=nums[j]
                nums[i]=curr
                k+=1
                i+=1
            j+=1
                
        return k