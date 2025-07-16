from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        index = n + m - 1
        n -= 1
        m -= 1

        while n >= 0:  
            if m>=0 and nums2[n] >= nums1[m]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
        
        return nums1

nums1=[2,0]
num2=[1]

print(merge(nums1,1,num2,1))


