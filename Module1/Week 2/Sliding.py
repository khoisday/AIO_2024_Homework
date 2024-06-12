def max_sliding(nums, k):
    if k < 1:
        return []

    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


print(max_sliding([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))
