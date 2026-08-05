def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def myPow(x, n):

    # if negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:

        # for odd exponent
        if n % 2 == 1:
            result = result * x

        # Square the base
        x = x * x

        # Divide exponent by 2 
        n = n // 2

    return result


nums = [1, 3, 5, 7, 9, 11]
target = 7

print(search(nums, target))


print(myPow(2.0, 10)) 
print(myPow(2.0, -2))