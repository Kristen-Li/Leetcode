```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quickSort(nums)
        # self.mergeSort(nums)
        # self.bubbleSort(nums)
        # self.insertionSort(nums)
		# self.selectionSort(nums)
        self.heapSort(nums)
        return nums
```
```
	# @bubbleSort, o(n^2)
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(1, n - i):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
```
```                    
	# @insertionSort, o(n^2)
    def insertionSort(self, nums): 
        for i in range(1, len(nums)): 
            while i -1 >= 0 and nums[i-1] > nums[i]:
              nums[i-1], nums[i] = nums[i], nums[i-1]
              i -= 1
        return nums
```
```
  # @shellSort, O(nlogn)
  def shell_sort(nums):
        n = len(nums)
        gap = n // 2
        while gap:
            for i in range(gap, n):
                while i - gap >= 0 and nums[i - gap] > nums[i]:
                    nums[i - gap], nums[i] = nums[i], nums[i - gap]
                    i -= gap
            gap //= 2
    return nums    
```
```
	# @selectionSort, o(n^2)
	def selectionSort(self, nums):
		for i in range(len(nums)):
			for j in range(i,len(nums)):
        if nums[j] < nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
		return nums
```
```
	# @quickSort
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums
```
```     
	# @mergeSort
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # 分
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        # 合并
        return merge(left, right)
```
```

    def merge(left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res
```
```
   # @heapSort
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
```
```
	#@ Quicksort
	def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums

    return quick(0, n - 1)
```
