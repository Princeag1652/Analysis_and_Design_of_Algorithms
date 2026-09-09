
def findKthLargest(nums, k):
    n = len(nums)

    # Selection sort in descending order
    for i in range(n):
        largest = i

        for j in range(i + 1, n):
            if nums[j] > nums[largest]:
                largest = j

        # Swap
        nums[i], nums[largest] = nums[largest], nums[i]

    return nums[k - 1]


def findMinMax(nums):
    minimum = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < minimum:
            minimum = nums[i]

        if nums[i] > maximum:
            maximum = nums[i]

    return minimum, maximum


# Example
nums = [3, 2, 1, 5, 6, 4]

print("2nd Largest:", findKthLargest(nums.copy(), 2))

minimum, maximum = findMinMax(nums)

print("Minimum:", minimum)
print("Maximum:", maximum)