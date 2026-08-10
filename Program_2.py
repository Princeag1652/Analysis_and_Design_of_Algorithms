class Sort:

    # Merge Sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return self.quick_sort(left) + middle + self.quick_sort(right)


# Example
s = Sort()

arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
print("Merge Sort:", s.merge_sort(arr))
print("Quick Sort:", s.quick_sort(arr))