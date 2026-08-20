class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num] = count.get(num,0) + 1
        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        
        return [x[1] for x in arr[-k:]]

